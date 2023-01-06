from django.shortcuts import render
from AllBlogs.models import Post        # getting this post form AllBlogs app 

# Create your views here.

def home (request):
    # sort posts according to date in descending order
    # this will make a whole then hit the database that's how this will not affect the performance of database
    latest_blogs = Post.objects.all().order_by("-date")[:3]   
    return render(request,'Home/home.html',{'latest_blogs':latest_blogs})  