# game_review/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class VideoGame(models.Model): 
    title = models.TextField(blank=False)
    genre = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date_released = models.DateField(blank=True, null=True)
    #removing rating attribute, using django @property instead
    #rating = models.FloatField(blank=True, null=True)
    developer = models.ForeignKey("Developer", on_delete=models.CASCADE)
    main_image = models.ImageField(blank=False)

    def __str__(self):
        return f'{self.title}, ({self.date_released})'
    
    def get_images(self):
        '''Retrieve all GameImages for this VideoGame'''
        images = GameImage.objects.filter(game=self)
        #print('debug', images)
        return images
    
    def get_reviews(self):
        '''Retrieve all Reviews for this VideoGame.'''
        reviews = Review.objects.filter(game=self)
        reviews = reviews.order_by('-date_reviewed')
        return reviews
    
    @property
    def rating(self):
        '''Calculate the rating for this VideoGame -- if there are no reviews for this game
        yet, the rating is "N/A" '''
        reviews = self.get_reviews()
        if len(reviews) == 0:
            return "N/A"
        avg_rating = 0
        for r in reviews: 
            avg_rating = avg_rating + r.rating
        avg_rating = avg_rating / len(reviews)
        avg_rating_rounded = format(avg_rating, '.2f')
        return avg_rating_rounded

    def get_absolute_url(self): 
        '''the URL to redirect to this game page'''
        return reverse("game", kwargs={ "pk": self.pk })

class Review(models.Model): 
    game = models.ForeignKey("VideoGame", on_delete=models.CASCADE)
    reviewer = models.ForeignKey("Reviewer", on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    rating = models.IntegerField(blank=False, default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    date_reviewed = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.game}, ({self.reviewer}), {self.rating}'
    
    def get_images(self): 
        '''Retrieve all ReviewImages for this VideoGame'''
        rev_images = ReviewImage.objects.filter(review=self)
        #print(images)
        #note: get_images currently returns a set of ReviewImages, 
        #need to do i.image to get the Image associated with ReviewImage, 
        #and then i.image.image_file to get the image file 
        #-- could make this more straightforward somehow?
        images = []
        for i in rev_images: 
            images.append(i.image)
        #note: this seems to work rn
        return images

class Reviewer(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(blank=False, default="reviewer")
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.name}'
    
    def get_my_reviews(self):
        '''Getting the Reviews written by this Reviewer'''
        my_reviews = Review.objects.filter(reviewer=self).order_by('-date_reviewed')
        return my_reviews

class Developer(models.Model): 
    name = models.TextField(blank=False)
    contact_info = models.TextField(default="contact_info")
    location = models.TextField(blank=True)
    description = models.TextField(blank=True)
    profile_img = models.ImageField(blank=True)
    
    def __str__(self):
        return f'{self.name}'
    
    def get_games(self):
        '''Retrieve all VideoGames associated with this Developer.'''
        games = VideoGame.objects.filter(developer=self)
        return games

#overall Image class 
class Image(models.Model): 
    image_file = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    #goal is to make it possible to add images to both games and reviews using this 
    
    def __str__(self):
        return f'{self.image_file}: {self.caption}'
    
#associating Images to VideoGames -- relationship between image and video game
class GameImage(models.Model):
    image  = models.ForeignKey("Image", on_delete=models.CASCADE)
    game = models.ForeignKey("VideoGame", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.game}, {self.image}'

#associating Images to Reviews 
class ReviewImage(models.Model):
    image = models.ForeignKey("Image", on_delete=models.CASCADE)
    review = models.ForeignKey("Review", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.review}, {self.image}'







