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
    def checkInReadLater(self,request,blog_id):
        # check this post is in read later section or not to show button
        stored_post_ids = request.session.get("stored_post_ids")
        exist_in_read_later = True                                  

        # is post id is not in stored_post_ids then will show the read later button on page
        if stored_post_ids is None or blog_id not in stored_post_ids:
            exist_in_read_later = False

        return exist_in_read_later


    def get(self,request,slug):                         # it also accept slug as arguement
        clicked_blog = Post.objects.get(slug=slug)       # remember get return a single object but filter return a queryset   
        context = {
                    "clicked_blog":clicked_blog,
                        "post_tags":clicked_blog.tags.all(),             # tags can have multiple entries
                            # sort the comments in decreasing order by id
                            "comments":clicked_blog.comments.all().order_by("-id"),        # access all the comments of this blog, its cross model queries
                                "comment_form":CommentForm(),              # initialise the form 
                                    "exist_in_RL":self.checkInReadLater(request,clicked_blog.id),
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
                            "comment_form":comment_form,                # return the same comment form
                                "exist_in_RL":self.checkInReadLater(request,clicked_blog.id)
                             }
        return render(request,"AllBlogs/blog_detail.html",context)


    
class ReadLater(View):
    def get(self,request):
        # get the list of ids of blogs which are set as read later 
        stored_post_ids = request.session.get("stored_post_ids")       
        context = {}                       # create a dictionary to pass in tempalte
        
        if stored_post_ids is None or len(stored_post_ids)==0:        # check is there any ids or not
            context["hasBlogs"] = False 
            context["blogs"] = []
    
        else:
            blogs = Post.objects.filter(id__in=stored_post_ids)     # it will return all post whose id is in store_post_ids
            context["hasBlogs"] = True
            context["blogs"] = blogs

        return render(request,"AllBlogs/read_later.html",context)


    def post(self,request):
        # access the stored id if it is first time then it return None
        stored_post_ids = request.session.get("stored_post_ids")       

        if stored_post_ids is None:     # if None then create a stored_post_ids list
            stored_post_ids = []

        # get the clicked_blog id which we need to save for read later
        blog_id = int(request.POST["clicked_blog_id"])        

        # if id of blog is not in list then add it 
        if blog_id not in stored_post_ids:
            stored_post_ids.append(blog_id)

        else:
            # if blog_id exist means this time user click for remove from read later button
            stored_post_ids.remove(blog_id)    

        # save the modification in session
        request.session["stored_post_ids"] = stored_post_ids
        
        return HttpResponseRedirect(reverse("allBlogs_page"))