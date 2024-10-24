from django.shortcuts import render

# Create your views here.
from . models import *
from . forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View #generic view
from django.shortcuts import redirect

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
        return reverse('profile', pk=self.kwargs['pk'])
    
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

        sm = form.save()
        files = self.request.FILES.getlist('files')
        #print('about to loop')
        for file in files: 
            image = Image.objects.create(status=sm, image_file=file)
            #print('made image')
            image.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs=self.kwargs)

class UpdateProfileView(UpdateView): 
    '''A view to show form used to update profile information'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

class DeleteStatusMessageView(DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status'
    
    def get_success_url(self):
        #print(self.object.profile.get_absolute_url())
        return self.object.profile.get_absolute_url()

class UpdateStatusMessageView(UpdateView): 
    '''A view to show form used to update status message information'''
    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'

    def get_success_url(self):
        #print(self.object.profile.get_absolute_url())
        return self.object.profile.get_absolute_url()
    
class CreateFriendView(View):
    '''A view to handle adding a friend to a profile '''
    def dispatch(self, request, *args, **kwargs):
        p1_pk = self.kwargs['pk']
        #print(p1_pk)
        p2_pk = self.kwargs['other_pk']
        #print(p2_pk)
        p1 = Profile.objects.get(pk=p1_pk)
        p2 = Profile.objects.get(pk=p2_pk)
        p1.add_friend(p2)

        #return super().dispatch(request, *args, **kwargs)
        kw_dict = {'pk': self.kwargs['pk']}
        url = reverse('profile', kwargs=kw_dict)
        return redirect(url)

class ShowFriendSuggestionsView(DetailView):
    '''A view to display suggested friends for a Profile'''
    template_name = 'mini_fb/friend_suggestions.html'
    model = Profile
    context_object_name = 'profile'
    
