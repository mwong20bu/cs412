#blog/views.py
#views to show the blog application
from django.shortcuts import render

from typing import Any #FIX: ADD MODULE NAME
from . models import *
from . forms import * 
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

import random 
 #generic view
# Create your views here.

#class based view
class ShowAllView(ListView): #inherits from listView class
    '''A view to show all Articles'''

    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'

class RandomArticleView(DetailView):
    '''Show one article selected at random.'''
    model = Article
    template_name = 'blog/article.html'
    context_object_name = "article" # note the singular name

    ## AttributeError: Generic detail view RandomArticleView must be called with either an object pk or a slug in the URLconf.
    ## one solution: implement the get_object method.
    def get_object(self):
        '''Return the instance of the Article object to show.'''

        # get all articles
        all_articles = Article.objects.all() # SELECT *
        # pick one at random
        return random.choice(all_articles)
    

class ArticleView(DetailView):
    '''Show one article by its primary key.
    On GET: sends back the form
    On POST: read the form data, create an instance of the model object, send to database'''

    model = Article
    template_name = 'blog/article.html'
    context_object_name = "article" # note the singular name

class CreateCommentView(CreateView):
    '''A view to show / process the create comment form'''

    form_class = CreateCommentForm
    template_name = 'blog/create_comment_form.html'
    
    def form_valid(self, form): 
        '''this method is called after the form is submitted, and checked to be complete with all fields'''

        print(form.cleaned_data) #used to see what was input in form
        print(self.kwargs) #used to see the kwargs

        article= Article.objects.get(pk=self.kwargs['pk']) #reading from dictionary, getting value with key pk --finding article number
        
        #now, attaching article to comment 
        #form.instance refers to the new comment that we're creating 
        form.instance.article = article 

        #this is for debugging 
        return super().form_valid(form)
    
    # what do we do after form submission
    def get_success_url(self) -> str:
        #return reverse('show_all')
        #when successful, show the article with the comment added
        return reverse('article', kwargs=self.kwargs) #need to specify primary key so we find the right article
    
    #def get_context_data(self, **kwargs: random.Any) -> dict[str, Any]:
     #   '''Build the dictionary of key-value pairs that will be passed into the template'''


      #  context = super().get_context_data(**kwargs)
        
        #add the article to the context data
       # article= Article.objects.get(pk=self.kwargs['pk'])
        #context['article'] = article

        #return context
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''
        build the template context data --
        a dict of key-value pairs.'''

        # get the super class version of context data
        context = super().get_context_data(**kwargs)

        # find the article with the PK from the URL
        # self.kwargs['pk'] is finding the article PK from the URL
        article = Article.objects.get(pk=self.kwargs['pk'])

        # add the article to the context data
        context['article'] = article

        return context