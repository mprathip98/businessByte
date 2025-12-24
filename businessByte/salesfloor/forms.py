from django import forms
from .models import Businesses

class BusinessesForm(forms.ModelForm):
    class Meta:
        model = Businesses
        fields = ["name", "image", "description", "address", "rating"]