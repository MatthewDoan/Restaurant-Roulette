from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from yelpapi import YelpAPI


apiKey ='nYjIQGRlDSimIZvPoagwvblHh_MhxAZJWDdd4fRlwfina_B_fOWL6rWbRkOhrq6a8KWT5xnsDVXD_mFKOZ30jbAMNrt3UZiOmMMxP81_Kn3z6KQOv8lpV-7aw4KaXnYx'


def base(request):
    return render(request, 'base.html', {})


@csrf_exempt
def postReq(request):
    yelp_api = YelpAPI(apiKey)
    longi = request.POST.get('longitude')
    lati = request.POST.get('latitude')
    response = yelp_api.search_query(latitude=lati, longitude=longi, limit=50)

    print(response)
    return JsonResponse(response)



