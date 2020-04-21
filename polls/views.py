from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import History

import random


import json

from yelpapi import YelpAPI


apiKey ='nYjIQGRlDSimIZvPoagwvblHh_MhxAZJWDdd4fRlwfina_B_fOWL6rWbRkOhrq6a8KWT5xnsDVXD_mFKOZ30jbAMNrt3UZiOmMMxP81_Kn3z6KQOv8lpV-7aw4KaXnYx'


def base(request):
    return render(request, 'base.html', {})

def history(request):
    return render(request, 'history.html', {'history':History.objects.all()})    


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
    if(Category == "asian"):
        categories = "asianfusion"
    if(Category == "american"):
        categories = "tradamerican"
    if(Category == "barbeque"):
        categories = "bbq"
    if(Category == "cafe"):
        categories = "cafes"
    if(Category == "fast food"):
        categories= "hotdogs"
    if(Category == "mediterranean"):
        categories= "mediterranean"
    if(Category == "vegan"):
        categories= "vegan"            


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
        
    if(total>50):
        total = 50
    randomNumber = random.randint(1,total) -1 
    print(randomNumber)
    print(jsonParsed1["businesses"][randomNumber])
    print(categories)


    randomRest = jsonParsed1["businesses"][randomNumber]
    final = {'img':randomRest["image_url"], 'name':randomRest["name"], 'address':randomRest["location"]["display_address"], 'phone':randomRest["display_phone"],'phone':randomRest["display_phone"]}
    h=History.objects.create(image = randomRest["image_url"], name = randomRest["name"], address1=randomRest["location"]["display_address"][0], address2=randomRest["location"]["display_address"][1], phone=randomRest["display_phone"], url=randomRest["url"])
    return JsonResponse(final)

