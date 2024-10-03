from django.db import models

# Create your models here.
class Article(models.Model):
    '''Encapsulate the data for a blog article by some author.'''

    #Data attributes 
    title = models.TextField(blank=False) #blank=False means you can't create an article without a title
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True) #automatically defined as current time when publishing
    image_url = models.URLField(blank=True) #new field : blank is default value, not mandatory
    
    def __str__(self):
        '''Return a string representation of this Article object, changes how articles are listed/named in admin interface'''
        return f'{self.title} by {self.author}'