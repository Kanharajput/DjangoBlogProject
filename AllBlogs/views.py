from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView
from .forms import CommentForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # object is the Blog which details are showing right now 
        # tags is many to many field that'swhy we are accessing all tags
        tags = self.object.tags.all()               
        context["post_tags"] = tags
        context["comment_form"] = CommentForm()
        return context
    
