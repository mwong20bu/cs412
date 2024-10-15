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
    
class Comment(models.Model):
    '''Encapsulate a comment on an article.'''

    # create a 1 to many relationship between Articles and Comments
    article = models.ForeignKey("Article", on_delete=models.CASCADE) ### IMPORTANT
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this object.'''
        return f'{self.text}'