#restaurant/views.py

from django.shortcuts import render
import random
from datetime import datetime, timedelta


# Create your views here.

daily_specials = [
    "3-meat BBQ Combo",
    "Roast Pork Congee",
    "Century Egg and Pork Congee ",
    "Beef Chow Fun",
    "Roast Duck Noodle",
    "Roast Pork Steamed Rice Rolls",
    "Egg Tarts",
]

images_list = [
    "../static/restaurant-images/cuihua.jpg",
    "../static/restaurant-images/menu.jpg",
    "../static/restaurant-images/dimsum.jpg",
]

costs = {
    "Roast Pork" : 8, 
    "Roast Duck" : 9, 
    "Soy Sauce Chicken" : 8, 
    "White Rice" : 2,
    "Substitute Brown Rice" : 1,
    "Substitute Fried Rice" : 2,
    "3-meat BBQ Combo" : 10, 
    "Roast Pork Congee" : 10,
    "Century Egg and Pork Congee " : 10,
    "Beef Chow Fun" : 10,
    "Roast Duck Noodle" : 10,
    "Roast Pork Steamed Rice Rolls" : 10,
    "Egg Tarts" : 10,
}
dt = datetime.now()
day_of_week = dt.weekday()

time_change = timedelta(minutes=(random.randint(30,60))) 
readytime = dt + time_change

def main(request):
    template_name = "restaurant/main.html"

    context = {
        'cuihua_img' : images_list[0],
        'menu_img' : images_list[1],
        'dimsum_img' : images_list[2],
    }

    return render(request, template_name, context)

def order(request): 
    template_name = "restaurant/order.html"

    context = {
        'daily_special' : daily_specials[day_of_week]
    }

    return render(request, template_name, context)
    
def confirmation(request):
    template_name = 'restaurant/confirmation.html'
    
    # check if the request is a POST (vs GET)
    if request.POST:

        # read the form data into python variables:
        name = request.POST['name']
        items = request.POST.getlist('items')
        total = 0
        for x in items: 
            total += costs[x]

        

        # package the data up to be used in response
        context = {
            'name': name,
            'items': items,
            'readytime' : readytime,
            'dt' : dt,
            'total': total,
        }

        # generate a response
        return render(request, template_name, context)