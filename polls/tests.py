from django.test import TestCase
from .models import History



class testing(TestCase):
    def setUp(self):
        test = {
            Category: "Any Category",
            Price: "1",
            Rating: 5,
            latitude: "",
            longitude: "",
            radius: ""
        }
    def testNoLatLong();
        self.assertEqual(postReq(test),'error')




