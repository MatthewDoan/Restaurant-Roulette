from django.test import TestCase
from .models import History
from .views import postReq


class testing(TestCase):
    def testNoLatLong(self):
        test = {
            'Category': "Any Category",
            'Price': "1",
            'Rating': 5,
            'latitude': "",
            'longitude': "",
            'radius': ""
        }
        self.assertEqual(postReq(test),errors=1)
