from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import MovieForm, CommentForm
from .models import Movie, Comment


# Create your views here.
@require_safe
def index(request):
    movies=Movie.objects.all()
    context={
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)

def update(request):
    pass

def delete(request):
    pass

def comments_create(request):
    pass

def comments_delete(request):
    pass