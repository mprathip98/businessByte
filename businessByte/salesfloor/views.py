from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

from .models import Businesses
from .forms  import BusinessesForm
from . import models
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F

def initial(request):
    return render(request, "home.html")





def dashboard(request):
    if request.user.is_authenticated:
        allBusinesses = Businesses.objects.all
        number_range = range(1, 6)
        if request.method == "POST":
            if request.POST.get("action") == "ratingForm":
                BusinessName = request.POST["busiName"]
                formRating = request.POST["rating"]
                business = get_object_or_404(Businesses, name=BusinessName)
                currentCount = business.ratingNumber
                currentSum = currentCount * business.rating
                newSum = currentSum + int(formRating)
                newCount = currentCount + 1
                newAverage = round(newSum/newCount)
                business.rating = newAverage
                business.ratingNumber = newCount
                business.save()
            elif request.POST.get("action") == "filterForm":
                filteredBusinesses = []

                try:
                    categoryFilter = request.POST["userCategory"]
                except MultiValueDictKeyError:
                    categoryFilter = ""
                try:
                    ratingFilter = request.POST["rating"]
                except MultiValueDictKeyError:
                    ratingFilter = ""

                if categoryFilter != "" and ratingFilter != "":
                    filteredBusinesses = Businesses.objects.filter(category=categoryFilter, rating=int(ratingFilter))
                elif ratingFilter != "":
                    filteredBusinesses = Businesses.objects.filter(rating=int(ratingFilter))
                elif categoryFilter != "":
                    filteredBusinesses = Businesses.objects.filter(category=categoryFilter)
                elif ratingFilter == "" and categoryFilter == "":
                    filteredBusinesses = allBusinesses

                allBusinesses = filteredBusinesses
            elif request.POST.get("action") == "favorite":
                business = request.POST["businessName"]
                userName = request.user.username



        return render(request, "dashboard.html", {"allBusinesses": allBusinesses, "number_range": number_range})
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


def favorites(request):
    return render(request, "favorites.html")

def coupons(request):
    return render(request, "coupons.html")