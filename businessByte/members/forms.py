from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#default forms for user registration
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        #needed fields for the user table
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

