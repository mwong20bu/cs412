from django.shortcuts import render

# Create your views here.
from . models import *
from . forms import *
from django.views.generic import ListView, DetailView, CreateView#generic view

# Create your views here.

#class based view
class ShowAllProfilesView(ListView): #inherits from listView class
    '''A view to show all profiles'''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'


class ShowProfilePageView(DetailView): 
    '''A view to show a single profile'''

    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    '''A view to show the CreateProfile form'''
    
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_absolute_url(self):
        '''Get the URL to show this Profile.'''
        return reverse('show_profile', pk=self.kwargs['pk'])
    
class CreateStatusMessageView(CreateView):
    '''A view to show the CreateProfile form'''
    
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        profile= Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.profile = profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs=self.kwargs)




    