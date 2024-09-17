## hw/urls.py 
## description: the app-specific URLS for the hw application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.home, name="home"), ##our first URL
]