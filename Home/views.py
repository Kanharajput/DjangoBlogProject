from django.shortcuts import render
from AllBlogs.models import Post        # getting this post form AllBlogs app 
from django.views.generic import ListView
# Create your views here.

class Home(ListView):
    model = Post
    template_name = "Home/home.html"
    ordering = ["-date"]               # sort the entries in decreasing order
    context_object_name = "latest_blogs"

    def get_queryset(self):
        base_query = super().get_queryset()
        three_items = base_query[:3]             # select the first three entries 
        return three_items
