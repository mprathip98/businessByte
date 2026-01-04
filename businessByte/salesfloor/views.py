from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
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
            BusinessName = request.POST["busiName"]
            formRating = request.POST["rating"]

            business = get_object_or_404(Businesses, name=BusinessName)

            currentCount = business.ratingNumber
            currentSum = currentCount * business.rating

            print(f"old sum = {currentSum}")
            print(f"old count = {currentCount}")


            newSum = currentSum + int(formRating)
            newCount = currentCount + 1
            print(newSum/newCount)
            print(round(newSum/newCount))
            newAverage = newSum/newCount


            print(f"new sum = {newSum}")
            print(f"new count = {newCount}")
            print(f"new average = {newAverage}")


            business.rating = newAverage
            business.ratingNumber = newCount

            business.save()


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