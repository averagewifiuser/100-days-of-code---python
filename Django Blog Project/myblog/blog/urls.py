from django.urls import path
from .views import (PostListView, 
PostCreateView, 
PostUpdateView, PostDeleteView, UserPostListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]