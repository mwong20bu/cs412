# voter_analytics/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.VotersListView.as_view(), name="home"),
    path(r'voters', views.VotersListView.as_view(), name='voters'),
    path(r'voter/<int:pk>', views.VoterDetailView.as_view(), name='voter_detail'),
    path(r'graphs', views.GraphListView.as_view(), name='graphs'),
]
