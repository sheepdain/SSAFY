from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.category_list),
    path('books/', views.book_list),
    path('books/<int:book_id>/', views.book_detail),
    path('books/<int:book_id>/threads/', views.article_list),
    path('books/<int:book_id>/threads/<int:thread_pk>/', views.article_detail),
    path('save_popular_books/', views.save_popular_books, name='save_popular_books'),
]
