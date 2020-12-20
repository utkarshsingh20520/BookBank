from django.urls import path
from . import views
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    UserBookListView,
)

urlpatterns = [
    path('', BookListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserBookListView.as_view(), name='user-posts'),
    path('post/<str:pk>/', BookDetailView.as_view(), name='post-detail'),
    path('post/new', BookCreateView.as_view(), name='post-create'),
    path('post/<str:pk>/update/', BookUpdateView.as_view(), name='post-update'),
    path('post/<str:pk>/delete/', BookDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
