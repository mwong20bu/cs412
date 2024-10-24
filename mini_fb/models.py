from django.db import models
from django.shortcuts import render
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data for a mini_fb profile'''

    #Data attributes 
    first_name = models.TextField(blank=False) #blank=False means you can't create an article without a title
    last_name = models.TextField(blank=False)
    email_address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True) #new field : blank is default value, not mandatory
    city = models.TextField(blank=False, default="Some Place")
    
    def __str__(self):
        '''Return a string representation of this Article object, changes how articles are listed/named in admin interface'''
        return f'{self.first_name} {self.last_name}'
    
    def get_status_message(self):
        '''Retrieve all status messages for this Profile.'''

        # use the ORM to filter StatusMessages where this 
        # instance of Profile is the FK
        status_messages = StatusMessage.objects.filter(profile=self)
        status_messages = status_messages.order_by('-timestamp')
        # status_messages = status_messages.order_by('-timestamp').values()
        return status_messages
    
    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after sucessful create'''
        #return "/blog/show_all"
        #return reverse("show_all")
        return reverse("profile", kwargs={ "pk": self.pk })
    
    def get_friends(self): 
        friends = Friend.objects.filter(profile1=self) | Friend.objects.filter(profile2=self)
        friends_prof = []
        for f in friends: 
            if f.profile1 == self: 
                friends_prof.append(f.profile2)
            else: 
                friends_prof.append(f.profile1)
        return friends_prof
    
    def add_friend(self, other):
        my_friends = self.get_friends()
        if other not in my_friends: 
            friendship = Friend.objects.create(profile1=self, profile2=other)
            friendship.save()
            #print("friendship added between", self, other)
        return 

    def get_friend_suggestions(self):
        my_friends = self.get_friends()
        print("my current friends:", my_friends)
        potentials = []
        for person in my_friends: 
            print(person)
            their_friends = person.get_friends()
            print("their friends:", their_friends)
            for p in their_friends: 
                if (p not in potentials) and (p != self): 
                    potentials.append(p)
        return potentials
        
    
class StatusMessage(models.Model):
    '''Encapsulate the data attributes for a facebook status message'''

    #Data attributes
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the status message object'''
        return f'{self.profile} {self.timestamp}'
    
    def get_image(self): 
        '''Retrieve all images for this StatusMessage.'''
        # use the ORM to filter Images where this 
        # instance of StatusMessage is the FK
        images = Image.objects.filter(status=self)
        #print('debug', images)
        return images
    
class Image(models.Model): 
    '''Encapsulate the data attributes for an image file'''
    #Data attributes
    timestamp = models.DateTimeField(auto_now=True)
    status = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)
    image_file = models.ImageField(blank=True)

    def __str__(self):
        '''Return a string representation of the Image object'''
        return f'{self.status} {self.image_file}'

class Friend(models.Model):
    '''Encapsulate the data attributes for a friend relationship between two Profiles'''
    timestamp = models.DateTimeField(auto_now=True)
    profile1 = models.ForeignKey("Profile", related_name="friendA", on_delete=models.CASCADE)
    profile2 = models.ForeignKey("Profile", related_name="friendB", on_delete=models.CASCADE)

    def __str__(self): 
        '''Returns a string representation of the Friend relationship'''
        p1 = self.profile1
        p2 = self.profile2
        return f'{p1.first_name} {p1.last_name} & {p2.first_name} {p2.last_name}'