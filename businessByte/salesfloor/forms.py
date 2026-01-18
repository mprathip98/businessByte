from django import forms
from .models import Businesses

#form structure for businesses
class BusinessesForm(forms.ModelForm):
    class Meta:
        model = Businesses
        #creating all the necessary fields for the business table
        fields = ["name", "image", "category", "description", "address", "rating"]

