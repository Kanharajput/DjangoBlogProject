from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView
# Create your views here.

# render the all_blogs html page
# LIstview to pass all entries in model to template
# by default dictionary name is object list
class ShowAllBlogs(ListView):
    model = Post
    template_name = "AllBlogs/all_blogs.html"
    

class BlogDetails(DetailView):
    template_name = "AllBlogs/blog_detail.html"
    model = Post
    context_object_name = "clicked_blog"

