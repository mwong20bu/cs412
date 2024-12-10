from django.contrib import admin

# Register your models here.
from .models import VideoGame, Review, Reviewer, Developer, Image, GameImage, ReviewImage
admin.site.register(VideoGame)
admin.site.register(Review)
admin.site.register(Reviewer)
admin.site.register(Developer)
admin.site.register(Image)
admin.site.register(GameImage)
admin.site.register(ReviewImage)