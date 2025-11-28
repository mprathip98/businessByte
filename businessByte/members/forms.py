from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']