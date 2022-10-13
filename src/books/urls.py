from django.urls import path
from books import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.BookList.as_view(), name='booklist'),
    path('books/<uuid:pk>/', views.BookDetail.as_view(), name='bookdetail'),
    path('author/', views.AuthorList.as_view(), name='authorlist'),
    path('author/<uuid:pk>/', views.AuthorDetail.as_view(), name='authordetail'),
]