
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('new_post', PostCreateView.as_view(), name = 'blog-new-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'blog-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'blog-delete'),

]
 