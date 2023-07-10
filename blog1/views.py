from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView    
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog1/post.html'
    context_object_name = 'post'
    ordering = ["-date_posted"]

    

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog1/detail.html' 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog1/post_form.html'
    fields =['title', 'content'] 

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form) 
    

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog1/post_form.html'
    fields =['title', 'content'] 

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)
    
    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return  True
        return False
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog1/delete.html'
    success_url = '/'

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return  True
        return False
