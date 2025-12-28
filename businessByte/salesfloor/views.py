from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Businesses
from .forms  import BusinessesForm


def initial(request):
    return render(request, "home.html")

def dashboard(request):
    if request.user.is_authenticated:
        allBusinesses = Businesses.objects.all



        return render(request, "dashboard.html", {"allBusinesses": allBusinesses})
    else:
        return redirect("home")

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BusinessesForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
            else:
                print(form.errors)
            messages.success(request, "Business Added")
            return redirect("dashboard")
        else:
            return render(request, "add.html")
    else:
            return redirect("home")


