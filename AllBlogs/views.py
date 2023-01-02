from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# render the all_blogs html page
def showAllBlogs(request):
    return render(request,'AllBlogs/all_blogs.html')

def blogDetails(request,blog_name):
    return render(request,'AllBlogs/blog_detail.html')