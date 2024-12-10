## mini_fb/urls.py 
## description: the app-specific URLS for the blog application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)
from django.contrib.auth import views as auth_views

# create a list of URLs for this app:
urlpatterns = [
    path('', views.ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path(r'profile/<int:pk>', views.ShowProfilePageView.as_view(), name="profile"), ## NEW
    path(r'create_profile', views.CreateProfileView.as_view(), name="create_profile"),
    path(r'profile/<int:pk>/create_status', views.CreateStatusMessageView.as_view(), name="create_status"),
    path(r'profile/<int:pk>/update', views.UpdateProfileView.as_view(), name="update_profile"),
    path(r'status/<int:pk>/delete', views.DeleteStatusMessageView.as_view(), name="delete_status"),
    path(r'status/<int:pk>/update', views.UpdateStatusMessageView.as_view(), name="update_status"),
    path(r'profile/<int:pk>/add_friend/<int:other_pk>', views.CreateFriendView.as_view(), name="create_friend"),
    path(r'profile/<int:pk>/friend_suggestions', views.ShowFriendSuggestionsView.as_view(), name="show_friend_suggestions"),
    path(r'profile/<int:pk>/news_feed', views.ShowNewsFeedView.as_view(), name="show_news"),
    path(r'login/', auth_views.LoginView.as_view(template_name='mini_fb/login.html'), name='login'), ## NEW
    path(r'logout/', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name='logout'), ## NEW
]