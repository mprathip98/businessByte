from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    return render(request, 'authenticate/login.html', {})

def logout_user(request):
    pass

def register_user(request):
    return render(request, "authenticate/register.html", {})
