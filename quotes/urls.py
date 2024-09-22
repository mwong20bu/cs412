## quotes/urls.py 
## description: the app-specific URLS for the quotes application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)

# create a list of URLs for this app:
urlpatterns = [
    #path(r'/', views.main, name="main"), ##the main page
    path(r'', views.quote, name="quote"),
    path(r'quote', views.quote, name="quote"), ## 
    path(r'show_all', views.show_all, name="show_all"), ## 
    path(r'about', views.about, name="about"), ## 
]