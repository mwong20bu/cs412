## mini_fb/urls.py 
## description: the app-specific URLS for the blog application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)

# create a list of URLs for this app:
urlpatterns = [
    path('', views.ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path(r'profile/<int:pk>', views.ShowProfilePageView.as_view(), name="profile"), ## NEW
    path(r'create_profile', views.CreateProfileView.as_view(), name="create_profile"),
    path(r'profile/<int:pk>/create_status', views.CreateStatusMessageView.as_view(), name="create_status"),
]