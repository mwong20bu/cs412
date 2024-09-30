## restaurant/urls.py 
## description: the app-specific URLS for the restaurant application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)

# create a list of URLs for this app:
urlpatterns = [
    path(r'main', views.main, name="main"), ##our first URL
    path(r'', views.main, name="main"),
    path(r'order', views.order, name="order"), ## new 
    path(r'confirmation', views.confirmation, name="confirmation"),
]