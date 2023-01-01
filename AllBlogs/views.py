from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def showAllBlogs(request):
    return HttpResponse("All blogs page")

def blogDetails(request,blog_name):
    return HttpResponse(str(blog_name) + " about this blog")