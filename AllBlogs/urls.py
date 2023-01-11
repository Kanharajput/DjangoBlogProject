from django.urls import path
from . import views


urlpatterns = [
    path('',views.ShowAllBlogs.as_view(),name="allBlogs_page"),                       # http://127.0.0.1:8000/allblogs/
    # DetailView can automatically match slug in url with slug in model and return the entry
    path("read-later",views.ReadLater.as_view(),name="read_later"),
    path('<slug:slug>',views.BlogDetails.as_view(),name="blogDetails_page"),            # http://127.0.0.1:8000/allblogs/blogname
]
