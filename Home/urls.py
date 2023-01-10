from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(), name="home_page"),           # http://127.0.0.1:8000/
]
