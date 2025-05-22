from django.shortcuts import render
from django.http import JsonResponse
from .utils import fetch_popular_books

def save_popular_books(request):
    fetch_popular_books()
    return JsonResponse({'status': 'ok', 'message': '베스트셀러 도서 100권 저장 완료'})

def category_list(request):
    pass
def book_list(request):
    pass
def book_detail(request):
    pass
def article_list(request):
    pass
def article_detail(request):
    pass
def create_comment(request):
    pass
def comment_detail(request):
    pass
