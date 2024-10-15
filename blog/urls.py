## blog/urls.py 
## description: the app-specific URLS for the blog application

from django.urls import path 
from django.conf import settings #importing settings for this project 
from . import views #from this local directory, import views (which refers to views.py file in this directory)

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.RandomArticleView.as_view(), name="random"), 
    path('show_all', views.ShowAllView.as_view(), name='show_all'),
    path(r'article/<int:pk>', views.ArticleView.as_view(), name="article"), ## NEW
    #path('create_comment', views.CreateCommentView.as_view(), name='create_comment'), ### FIRST (WITHOUT PK)
    path(r'article/<int:pk>/create_comment', views.CreateCommentView.as_view(), name="article"), ## now adding primary key to create comment URL
]