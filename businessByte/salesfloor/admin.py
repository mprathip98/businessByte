from django.contrib import admin
from .models import Businesses, userFavoritesBusiness

# Register your models here.
admin.site.register(Businesses)
admin.site.register(userFavoritesBusiness)
