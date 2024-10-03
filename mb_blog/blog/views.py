from django.shortcuts import render
from blog.models import *
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
# Create your views here.
class homepageview(ListView):
    model = Blog
    template_name = 'blog/index.html'
    
class contactpageview(CreateView):
    model = contactform
    template_name = 'blog/contact.html'
    fields= '__all__'
    
class categorypageview(ListView):
    model = Blog
    template_name = 'blog/category.html'
    
class search_resultpageview(ListView):
    model = Blog
    template_name = 'blog/search_result.html'
    
class single_postpageview(ListView):
    model = Blog
    template_name = 'blog/single_post.html'
    
class aboutpageview(ListView):
    model = Blog
    template_name = 'blog/about.html'
    
class BlogDetailView(DetailView):
    model = Blog 
    template_name = 'blog/detail.html'
class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/create.html'
    fields=['title', 'author', 'body']
class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/edit.html'
    fields=['title', 'author', 'body']
class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')
    