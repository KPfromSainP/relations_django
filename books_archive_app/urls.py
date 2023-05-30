from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.index),
    path('api/book', views.BookListCreate.as_view()),
    path('api/book_instance', views.BookInstanceListCreate.as_view()),
    path('api/genre', views.GenreListCreate.as_view()),
    path('api/author', views.AuthorListCreate.as_view()),
]