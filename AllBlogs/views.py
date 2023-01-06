from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

# removed the data local data now the data is fetched from database
# render the all_blogs html page
def showAllBlogs(request):
    posts = Post.objects.all()
    return render(request,'AllBlogs/all_blogs.html',{"all_blogs":posts})

def blogDetails(request,blog_name):
    # post = Post.objects.get(slug=blog_name) if post not found so return 404 template
    post = get_object_or_404(Post, slug=blog_name)
    tags = post.tags.all()               # getting all tag entries related with this post as a list
    return render(request,
                    'AllBlogs/blog_detail.html',
                        {"clicked_blog":post, "post_tags":tags} 
                    )