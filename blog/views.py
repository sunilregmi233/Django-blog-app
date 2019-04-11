from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class BlogPostView(ListView):
    model = Post
    template_name='home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name='post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
class BlogUpdateView(UpdateView):
    model=Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']