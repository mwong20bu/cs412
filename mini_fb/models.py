from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data for a blog article by some author.'''

    #Data attributes 
    first_name = models.TextField(blank=False) #blank=False means you can't create an article without a title
    last_name = models.TextField(blank=False)
    email_address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True) #new field : blank is default value, not mandatory
    city = models.TextField(blank=False, default="Some Place")
    
    def __str__(self):
        '''Return a string representation of this Article object, changes how articles are listed/named in admin interface'''
        return f'{self.first_name} {self.last_name}'