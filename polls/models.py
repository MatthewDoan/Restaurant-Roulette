from django.db import models

# Create your models here.

class History(models.Model):
    image = models.CharField(max_length=500, default='0000000')
    address1 = models.CharField(max_length=500, default='0000000')
    address2 = models.CharField(max_length=500, default='0000000')
    url = models.CharField(max_length=500, default='0000000')
    name = models.CharField(max_length=50, default='0000000')
    phone = models.CharField(max_length=50, default='0000000')
