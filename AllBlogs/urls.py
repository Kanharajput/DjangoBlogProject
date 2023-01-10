from django.urls import path
from . import views


urlpatterns = [
    path('',views.ShowAllBlogs.as_view(),name="allBlogs_page"),                       # http://127.0.0.1:8000/allblogs/
    path('<str:blog_name>',views.blogDetails,name="blogDetails_page")            # http://127.0.0.1:8000/allblogs/blogname
]
