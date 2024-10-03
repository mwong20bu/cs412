from django.shortcuts import render

# Create your views here.
from . models import *
from django.views.generic import ListView #generic view
# Create your views here.

#class based view
class ShowAllProfilesView(ListView): #inherits from listView class
    '''A view to show all Articles'''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'