# mini_fb/forms.py

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create Profile data.'''

    class Meta:
        '''associate this form witht he Profile model'''
        model = Profile
        
        fields = ['first_name', 'last_name', 'email_address', 'profile_image_url', 'city']

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create StatusMessage data.'''

    class Meta:
        '''associate this form witht he Profile model'''
        model = StatusMessage

        fields = ['message']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update Profile data'''

    class Meta:
        '''associate this form with the Profile model'''
        model = Profile
        
        fields = ['email_address', 'profile_image_url', 'city']

class UpdateStatusMessageForm(forms.ModelForm):
    '''A form to update StatusMessage message data'''

    class Meta:
        '''associate this form with the StatusMessage model'''
        model = StatusMessage
        
        fields = ['message']