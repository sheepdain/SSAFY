from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import (
    require_http_methods,
    require_safe,
    require_POST,
)
from django.contrib.auth.decorators import login_required

from accounts.models import Category
from .models import Book, Thread, Comment
from .forms import ThreadForm, CommentForm
from .utils import (
    generate_image_with_openai,
    get_or_create_book_vectors, recommend_similar_books
)


# Index 페이지
@require_safe
def index(request):
    now_category = request.GET.get('category')
    if now_category:
        books = Book.objects.filter(category__name=now_category)
    else:
        books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories,
        'now_category': now_category,
    }
    return render(request, 'books/index.html', context)


# 장르별 필터링
@require_safe
def filter_category(request):
    category = request.GET.get("category")
    
    if category:
        books = Book.objects.filter(category__name=category)
    else:
        books = Book.objects.all()

    books_data = []
    for book in books:
        books_data.append({
            'id': book.id,
            'title': book.title,
            'description': book.description,
            'cover': book.cover.url if book.cover else '',
        })

    return JsonResponse({'books': books_data})


@require_safe
def detail(request, book_pk):
    books = Book.objects.all()
    vectors = get_or_create_book_vectors(books)

    book = Book.objects.get(pk=book_pk)
    target_idx = list(books).index(book)

    rec_idxs = recommend_similar_books(target_idx, vectors)
    recommended_books = [books[i] for i in rec_idxs]

    return render(request, "books/detail.html", {
        "book": book,
        "recommended_books": recommended_books,
    })

@login_required
@require_http_methods(["GET", "POST"])
def thread_create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.book = book
            thread.user = request.user
            thread.save()

            generated_image_path = generate_image_with_openai(thread.title, thread.content, book.title, book.author)
            if generated_image_path:
                thread.cover_img = generated_image_path
                thread.save()
                
            return redirect("books:thread_detail", book.pk, thread.pk)
    else:
        form = ThreadForm()
    context = {
        "form": form,
        "book": book,
    }
    return render(request, "books/thread_create.html", context)


@login_required
@require_safe
def thread_detail(request, book_pk, thread_pk):
    book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    comment_form = CommentForm()
    context = {
        "book" : book,
        "thread": thread,
        "comment_form" : comment_form,
    }
    return render(request, "books/thread_detail.html", context)



@login_required
@require_http_methods(["GET", "POST"])
def thread_update(request, book_pk, thread_pk):
    book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    comment_form = CommentForm(request.POST)
    if thread.user == request.user:
        if request.method == "POST":
            form = ThreadForm(request.POST, request.FILES, instance=thread)
            if form.is_valid():
                form.save()  
                return redirect('books:thread_detail', book_pk=book.pk, thread_pk=thread.pk)
        else:
            form = ThreadForm(instance=thread)
    else :
        return redirect('books:index') 
    context = {
        "form": form,
        "book": book,
        "comment_form" : comment_form,
    }
    return render(request, "books/thread_update.html", context)


@login_required
@require_POST
def thread_delete(request, book_pk, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    if thread.user == request.user:
        thread.delete()
    return redirect("books:detail", book_pk)


# 쓰레드 좋아요 비동기 처리
@login_required
@require_POST
def likes(request, book_pk, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    if thread.likes.filter(pk=request.user.pk).exists():
        thread.likes.remove(request.user)
        is_like = False
    else:
        thread.likes.add(request.user)
        is_like = True
    context = {
        'is_like': is_like,
        'likes_count': thread.likes.count(),
    }
    return JsonResponse(context)

# 쓰레드 댓글 비동기 처리
@login_required
@require_POST
def create_comment(request, book_pk, thread_pk):
    
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.thread = Thread.objects.get(pk=thread_pk)
        comment.user = request.user
        comment.save()
    
        context = {
            'comment_id': comment.pk,
            'content': comment.content,
            'username': comment.user.username,
            'is_owner': True,
        }

        return JsonResponse(context)
    context = {
        'error': 'invalid form'
    }
    return JsonResponse(context, status=400)
    

@login_required
@require_POST
def delete_comment(request, book_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
        context = {
            'status': 'deleted',
        }
        return JsonResponse(context)
    context = {
        'error': '권한 없음'
    }
    return JsonResponse(context, status=403)