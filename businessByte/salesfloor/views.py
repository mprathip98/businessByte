from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def initial(request):
    return render(request, "home.html")

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        return redirect("home")

def add(request):
    if request.user.is_authenticated:
        return render(request, "add.html")
    else:
        return redirect("home")


