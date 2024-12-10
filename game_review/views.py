#game_review/views.py 

from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from . models import *
from . forms import *

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class LoggedInReviewerView(View): 
    '''A class for adding the logged_in_review context variable to the base template, 
    to be inherited by all other classes so that logged in reviewer's page is shown on nav menu'''
    template_name = "game_review/base.html"

    def get_context_data(self, **kwargs):
        '''Adding logged_in_reviewer to the context data'''
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated: 
            r = Reviewer.objects.get(user=self.request.user)
            context['logged_in_reviewer'] = r
        return context

#class based view
class ShowAllVideoGamesView(LoggedInReviewerView, ListView): #inherits from listView class
    '''A view to show all video games'''

    model = VideoGame
    template_name = 'game_review/show_all_games.html'
    context_object_name = 'videogames'

    def dispatch(self, request):
        '''add this method to show/debug logged in user'''
        print(f"Logged in user: request.user={request.user}")
        print(f"Logged in user: request.user.is_authenticated={request.user.is_authenticated}")
        return super().dispatch(request)

class ShowVideoGameView(LoggedInReviewerView, DetailView):
    '''A view to show a single video game'''
    model = VideoGame
    template_name = 'game_review/show_game.html'
    context_object_name = 'v'

class ShowDeveloperView(LoggedInReviewerView, DetailView):
    '''A view to show a Developer'''
    model = Developer
    template_name = 'game_review/developer.html'
    context_object_name = "developer"

class CreateReviewView(LoginRequiredMixin, LoggedInReviewerView, CreateView):
    '''A view to show the CreateReview form'''
    
    form_class = CreateReviewForm
    template_name = 'game_review/create_review_form.html'

    def get_login_url(self) -> str:
        '''return the URL required for login -- if the user is not logged in, attempting 
        to access the create_review url will redirect to the login page'''
        return reverse('login')
    
    def get_context_data(self, **kwargs):
        '''Adding the VideoGame that is being reviewed to the context data'''
        context = super().get_context_data(**kwargs)
        game = VideoGame.objects.get(pk=self.kwargs['pk'])
        context['game'] = game
        return context
    
    def form_valid(self, form):
        #attaching the game that this review is for to the Review instance being created
        game= VideoGame.objects.get(pk=self.kwargs['pk'])
        form.instance.game = game

        #attaching the current user to the Review instance
        user = self.request.user
        form.instance.user = user

        #print("type of user", type(user)) -- debugging
        #print(self.request.user.pk) -- debugging

        #attaching the current user as the Reviewer for the Review instance being created
        reviewer = Reviewer.objects.get(user=self.request.user.pk)
        #print(reviewer) -- debugging
        form.instance.reviewer = reviewer

        #saving the newly created Review instance
        r = form.save()

        #saving the images being added to the Review
        files = self.request.FILES.getlist('files')
        for file in files: 
            #note: how to add caption field and associate it with the specific image uploaded?
            image = Image.objects.create(image_file=file, caption="tester for now")
            # (RESOLVED) note: how to handle Images? If all ReviewImages are part of the Image class, are images added to form assigned to be Image or ReviewImage
            reviewimage = ReviewImage.objects.create(review=r, image=image)
            #print('made image')
            reviewimage.save()
        return super().form_valid(form)

    def get_success_url(self):
        '''upon successful creation, goes back to the page of the VideoGame being reviewed'''
        return reverse('game', kwargs=self.kwargs)
    
class DeleteReviewView(LoginRequiredMixin, LoggedInReviewerView, DeleteView):
    '''A view for deleting a review'''
    model = Review
    template_name = 'game_review/delete_review_form.html'
    context_object_name = 'r'
    
    def get_success_url(self):
        return self.object.game.get_absolute_url()

class UpdateReviewView(LoginRequiredMixin, LoggedInReviewerView, UpdateView): 
    '''A view for updating a review's content'''
    model = Review
    form_class = UpdateReviewForm
    template_name = 'game_review/update_review_form.html'

    def get_success_url(self):
        return self.object.game.get_absolute_url()
    
class SearchGameView(LoggedInReviewerView, ListView): 
    '''View to display search options and results for VideoGame searching'''
    template_name = "game_review/search_games.html"
    model = VideoGame
    context_object_name = "games"

    def get_queryset(self):
        '''Return the set of Results '''
        #use the superclass version of the queryset
        qs = super().get_queryset()
        #print(qs) -- for debugging

        #adding filter parameters
        #filtering by title: 
        if 'title' in self.request.GET:
            title = self.request.GET['title']
            #print("title is", title)
            if title: 
                qs = qs.filter(title__icontains=title)
        #print("after filtering title", qs)
        
        #filtering by genre
        if 'genre' in self.request.GET:
            genre = self.request.GET['genre']
            #print("genre is", genre)
            if genre:
                qs = qs.filter(genre__icontains=genre)
        #print("after filtering genre", qs)
        
        """ Working on adding a rating filter, but not sure how to implement, since rating is a property and not an attribute
        if 'rating' in self.request.GET:
            rating = self.request.GET['rating']
            print("rating is", rating)
            if rating == "":
                qs = qs
            else:
                rating = float(rating)
                for game in qs:
                    print(game, "rating:", game.get_rating()) 
                    print(game.get_rating()=="N/A")
                    print("game rating type", type(game.get_rating()), "vs rating type", type(rating))
                    if game.get_rating() == "N/A":  
                        
                    if game.get_rating() >= rating: 
                        continue
                    else: 
                        qs.pop()
        print("after filtering rating", qs)"""

        return qs

class CreateReviewerView(LoggedInReviewerView, CreateView):
    '''A view to create a Reviewer'''
    form_class = CreateReviewerForm
    template_name = 'game_review/create_reviewer_form.html'
    model = Reviewer

    def get_context_data(self, **kwargs):
         '''Adding the UserCreationForm to the CreateReviewerForm -- clients will create a User
         in the Reviewer creation process, the credentials of which will be used to log in'''
         context = super().get_context_data(**kwargs)
         context['userform'] = UserCreationForm
         return context
    
    def get_queryset(self):
        return Reviewer.objects.filter(user=self.request.user)
    
    def form_valid(self, form): 
        #getting current user, this was used for debugging 
        user = self.request.user

        #this was used for debugging
        for key, value in self.request.POST.items():
            if isinstance(value, bytes): 
                print(f"found byte data in (key): (value)")

        if user.is_authenticated: 
            form.instance.user = user
            return super().form_valid(form)
        
        #creating new User and attaching it to newly created Reviewer
        else:
            #reconstructing the UserCreationForm instance from the self.request.POST data
            user_form = UserCreationForm(self.request.POST)

            #if the UserCreationForm is valid, save the newly created User instance and attach it 
            #to the Reviewer instance being created
            if user_form.is_valid():
                user=user_form.save()
                form.instance.user = user 
                print("User created: (user), Reviewer.user:(form.instance.user)")
                return super().form_valid(form)
            else: 
                print("form was invalid")
                print("form errors:", user_form.errors)
                return self.form_invalid(form)

    def get_success_url(self):
        return reverse('reviewer', kwargs={'pk': self.object.pk})

class ShowReviewerView(LoggedInReviewerView, DetailView):
    '''A class to show a Reviewer's page'''
    model = Reviewer
    template_name = 'game_review/show_reviewer.html'
    context_object_name = 'reviewer'
    
class UpdateReviewerView(LoginRequiredMixin, LoggedInReviewerView, UpdateView): 
    '''A class to update a Reviewer's attributes'''
    model = Reviewer
    template_name = 'game_review/update_reviewer_form.html'
    form_class = UpdateReviewerForm

    def get_success_url(self):
        return reverse('reviewer', kwargs={'pk': self.object.pk})
