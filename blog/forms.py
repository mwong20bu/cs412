# blog/form.py

from django import forms
from .models import Comment

class CreateCommentForm(forms.ModelForm):
    '''A form to add a Comment to the database.'''

    class Meta: #meta information -- this is the name Django is expecting 
        '''associate this form with the Comment model, select fields.'''
        model = Comment # creates instances of Comment
        
        fields = ['author', 'text', ]  # which fields from model should we use -- changeable later
