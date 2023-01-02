from django.shortcuts import render
from .Helper.BlogDetailsData import all_blogs
# Create your views here.

# render the all_blogs html page
def showAllBlogs(request):
    return render(request,'AllBlogs/all_blogs.html',{'all_blogs':all_blogs})

def blogDetails(request,blog_name):
    return render(request,'AllBlogs/blog_detail.html')