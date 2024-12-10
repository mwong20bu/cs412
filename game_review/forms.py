# game_review/forms.py
# contains the ModelForms for creating / updating / deleting model instances in the game_review app

from django import forms
from .models import *

class CreateReviewForm(forms.ModelForm):
    '''A form to create Review data.'''
    class Meta:
        '''associate this form with the Review model'''
        model = Review
        fields = ['content', 'rating']

class UpdateReviewForm(forms.ModelForm):
    '''A form to update Review data.'''
    class Meta:
        '''the Review's content and rating can be changed'''
        model = Review
        fields = ['content', 'rating']

class CreateReviewerForm(forms.ModelForm):
    '''A form to create Reviewer data.'''
    class Meta:
        '''associate this form with the Reviewer model'''
        model = Reviewer
        fields = ['name', 'bio', 'profile_img']

class UpdateReviewerForm(forms.ModelForm):
    '''A form to update Reviewer data.'''
    class Meta:
        '''Reviewers can make changes to their profile picture and bio'''
        model = Reviewer
        fields = ['bio', 'profile_img']