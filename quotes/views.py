## quotes/view.py
## description: the logic to handle URL requests 
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time 
import random

# Create your views here.

quotes = [
    "If you only read the books that everyone else is reading, you can only think what everyone else is thinking.",
    "Memories warm you up from the inside. But they also tear you apart.", 
    "And once the storm is over, you won’t remember how you made it through, how you managed to survive. You won’t even be sure, whether the storm is really over. But one thing is certain. When you come out of the storm, you won’t be the same person who walked in. That’s what this storm’s all about.",
    "Pain is inevitable. Suffering is optional.",
    "Whatever it is you're seeking won't come in the form you're expecting.",
    "Why do people have to be this lonely? What's the point of it all? Millions of people in this world, all of them yearning, looking to others to satisfy them, yet isolating themselves. Why? Was the earth put here just to nourish human loneliness?",
    "Silence, I discover, is something you can actually hear.",
    "Listen up - there's no war that will end all wars.",
    "Despite your best efforts, people are going to be hurt when it's time for them to be hurt.",
]

images = [
    "../static/quote-images/murakami_books.jpg",
    "../static/quote-images/murakami_pic.jpg",
    "../static/quote-images/murakamib&w.jpg",
]

def quote(request):
    '''
    A function to respond to the /quote URL.
    This function will delegate work to the quote.html HTML template.
    '''

    template_name = "quotes/quote.html"

    context = {
        'selected_quote' : quotes[random.randint(0,len(quotes)-1)], #randomly select a quote from quote list
        'selected_image' : images[random.randint(0,len(images)-1)], #randomly select an image from image list
    }
    
    return render(request, template_name, context) #request is the parameter passed into home function above



def show_all(request):
    '''
    A function to respond to the /show_all URL.
    This function will delegate work to show_all.html HTML template.
    '''
    template_name = "quotes/show_all.html"
    context = {
        'quote0' : quotes[0],
        'quote1' : quotes[1],
        'quote2' : quotes[2],
        'quote3' : quotes[3],
        'quote4' : quotes[4],
        'quote5' : quotes[5],
        'quote6' : quotes[6],
        'quote7' : quotes[7],
        'quote8' : quotes[8],
        'image0' : images[0],
        'image1' : images[1],
        'image2' : images[2],
    }
    return render(request, template_name, context) #request is the parameter passed into home function above


def about(request):
    '''
    A function to respond to the /about URL.
    This function will delegate work to about.html HTML template.
    '''
    template_name = "quotes/about.html"
    context = {

    }
    return render(request, template_name, context) #request is the parameter passed into home function above