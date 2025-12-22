from django.db import models

# Create your models here.
class Businesses(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='businesses/')
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rating = models.FloatField()


