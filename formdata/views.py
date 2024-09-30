# formdata/view.py
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def show_form(request):
    '''Show the HTML form to the client.'''

    # use this template to produce the response
    template_name = 'formdata/form.html'
    return render(request, template_name)


def submit(request):
    '''Handle the form submission.
    Read out the formm data.
    Generate a response.'''
    template_name = 'formdata/confirmation.html'

    print(request)
    # check if the request is a POST (vs GET)
    if request.POST: 

        #read the form data into python variables
        name = request.POST['name']
        favorite_color = request.POST['favorite_color']

        # package data from the request, to be used in response
        context = {
            'name': name,
            'favorite_color': favorite_color,
        }

        #generate a response
        return render(request, template_name, context)
    
    # GET request lands down here: no return statements!

    #this is an okay solution: graceful error
    #return HttpResponse("Nope.")

    #this is a better solution, but shows wrong url
    # if the client got here by making a GET on this url, send back the form 
    #template_name = 'formdata/form.html'
    #return render(request, template_name)

    #ideally, do this: *redirect* to correct url (the form)
    return redirect("show_form")