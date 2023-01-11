from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView,View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# render the all_blogs html page
# LIstview to pass all entries in model to template
# by default dictionary name is object list
class ShowAllBlogs(ListView):
    model = Post
    template_name = "AllBlogs/all_blogs.html"
    

class BlogDetails(View):
    def get(self,request,slug):                         # it also accept slug as arguement
        clicked_blog = Post.objects.get(slug=slug)       # remember get return a single object but filter return a queryset                   
        context = {
                    "clicked_blog":clicked_blog,
                        "tags":clicked_blog.tags.all(),             # tags can have multiple entries
                            # sort the comments in decreasing order by id
                            "comments":clicked_blog.comments.all().order_by("-id"),        # access all the comments of this blog, its cross model queries
                                "comment_form":CommentForm()              # initialise the form 
                             }
        return render(request,"AllBlogs/blog_detail.html",context)


    # as this post method is coming from the same url that is blogDetails_page 
    # and this url also need a slug means by default this request contains the slug
    def post(self,request,slug):
        clicked_blog = Post.objects.get(slug=slug)
        # directly fetch the form from the POST request
        comment_form = CommentForm(request.POST) 
        # check it's valid , if valid save the form data
        # directly save data as it's a model form
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)        # not save to database initiate the comment object with user entered data
            comment.post = clicked_blog                   # manually link comment with the blog
            comment.save()                                # save to the database
            return HttpResponseRedirect(reverse("blogDetails_page", args=[slug])) # return to this same url again

        # FORM NOT VALID, then return to the same page with data to the fields which is already entered by the user
        context = {
                    "clicked_blog":clicked_blog,
                        "tags":clicked_blog.tags.all(),             
                            "comment_form":comment_form                # return the same comment form
                             }
        return render(request,"AllBlogs/blog_detail.html",context)


    
