from django.urls import path
from . import views


urlpatterns = [
    path('',views.showAllBlogs),                       # http://127.0.0.1:8000/allblogs/
    path('<str:blog_name>',views.blogDetails)            # http://127.0.0.1:8000/allblogs/blogname
]
