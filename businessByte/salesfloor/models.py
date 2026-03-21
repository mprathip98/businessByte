from django.db import models

# business model.
class Businesses(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='businesses/')
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rating = models.IntegerField(null=True , blank=True, default=0)
    ratingNumber = models.IntegerField(null=True , blank=True, default=0)

#favorites model
class userFavoritesBusiness(models.Model):
    name = models.CharField(max_length=100)
    business = models.CharField(max_length=100)