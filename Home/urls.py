from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),           # http://127.0.0.1:8000/
]
