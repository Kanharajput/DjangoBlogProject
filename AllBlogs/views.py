from django.shortcuts import render
from django.http import HttpResponse
from Home.Helper.BlogDetailsData import all_blogs       # directly getting it from home app
# Create your views here.

# render the all_blogs html page
def showAllBlogs(request):
    return render(request,'AllBlogs/all_blogs.html',{'all_blogs':all_blogs})

def blogDetails(request,blog_name):
    for clicked_blog in all_blogs:
        if clicked_blog['slug'] == blog_name:
            return render(request,'AllBlogs/blog_detail.html',{'clicked_blog':clicked_blog})

    else:
        return HttpResponse("page not found")