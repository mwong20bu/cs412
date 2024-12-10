# game_review/urls.py 
# the app-specific URLS for the game_review application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)
from django.contrib.auth import views as auth_views

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.ShowAllVideoGamesView.as_view(), name='all_games'),
    path(r'game/<int:pk>', views.ShowVideoGameView.as_view(), name='game'),
    path(r'developer/<int:pk>', views.ShowDeveloperView.as_view(), name='developer'),
    path(r'game/<int:pk>/create_review', views.CreateReviewView.as_view(), name="create_review"),
    path('login/', auth_views.LoginView.as_view(template_name='game_review/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='game_review/logout.html'), name="logout"),
    path(r'game/<int:pk>/delete', views.DeleteReviewView.as_view(), name="delete_review"),
    path(r'game/<int:pk>/update', views.UpdateReviewView.as_view(), name="update_review"),
    path(r'search_game/', views.SearchGameView.as_view(), name='search_game'),
    path(r'create_reviewer/', views.CreateReviewerView.as_view(), name='create_reviewer'),
    path(r'reviewer/<int:pk>', views.ShowReviewerView.as_view(), name='reviewer'), 
    path(r'reviewer/<int:pk>/edit', views.UpdateReviewerView.as_view(), name='edit_reviewer'), 
]
