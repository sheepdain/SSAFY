from django.urls import path
from . import views

app_name='memo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:note_pk/delete', views.delete, name='delete'),
    path('<int:note_pk/', views.detail, name='detail'),

]