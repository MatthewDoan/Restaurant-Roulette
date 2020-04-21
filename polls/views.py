from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import random


import json

from yelpapi import YelpAPI


apiKey ='nYjIQGRlDSimIZvPoagwvblHh_MhxAZJWDdd4fRlwfina_B_fOWL6rWbRkOhrq6a8KWT5xnsDVXD_mFKOZ30jbAMNrt3UZiOmMMxP81_Kn3z6KQOv8lpV-7aw4KaXnYx'


def base(request):
    return render(request, 'base.html', {})

def history(request):
    return render(request, 'history.html', {})    


@csrf_exempt
def postReq(request):
    yelp_api = YelpAPI(apiKey)
    longi = request.POST.get('longitude')
    lati = request.POST.get('latitude')
    rating = str(request.POST.get('Rating'))
    radius = request.POST.get('radius')
    Category = request.POST.get('Category').lower()
    Price = int(request.POST.get('Price'))
    print(longi,lati,rating,radius,Category,Price)

    #Required
    query = ""



    #Optional
    if(radius != ""):
        radius = int(radius) * 1609.34
        if(radius > 40000):
            radius = 40000
    if(radius == ""):
        radius = 40000
    
     
 
    print(Category)
    if(Category == 'any category<div class="ripple-container"></div>' or Category == "any category"):
        categories = "restaurants"
    else:
        categories = Category

    if(Price == 1 or Price == 5):
        Prices = "1,2,3,4"
    if(Price == 2):
        Prices = "2,3,4"
    if(Price == 3):
        Prices = "3,4"
    if(Price == 4):
        Prices = "4"


    print(Prices,categories,longi, lati, radius)

    response = yelp_api.search_query(price=Prices, categories=categories, radius=radius, longitude=longi, latitude=lati,limit=50)

    jsonParsed = json.dumps(response)
    jsonParsed1 = (json.loads(jsonParsed))
    total = jsonParsed1["total"]
    print(total)

    randomNumber = random.randint(1,50) -1 
    print(randomNumber)
    print(jsonParsed1["businesses"][randomNumber])

    randomRest = jsonParsed1["businesses"][randomNumber]
    final = {'img':randomRest["image_url"], 'name':randomRest["name"], 'address':randomRest["location"]["display_address"], 'phone':randomRest["display_phone"]}
    return JsonResponse(final)



#Italian, Chinese/Asian, American, mediterranean, mexican, Fast food, Vegan, cafe, Barbeque 
#meals 3 

# Rating: 3
# latitude: 42.960119999999996
# longitude: -85.9063455
# radius: 20
# Category: Asian
# Price: 3