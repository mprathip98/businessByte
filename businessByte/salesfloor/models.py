from django.db import models

# Create your models here.
class Businesses(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='businesses/')
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rating = models.IntegerField(null=True , blank=True, default=0)
    ratingNumber = models.IntegerField(null=True , blank=True, default=0)



