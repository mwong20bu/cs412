## blog/urls.py 
## description: the app-specific URLS for the blog application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)

# create a list of URLs for this app:
urlpatterns = [
    path('', views.ShowAllView.as_view(), name='show_all'),
]