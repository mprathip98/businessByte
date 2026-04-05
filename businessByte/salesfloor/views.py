# all of the libraries needed
from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .models import Businesses
from .forms  import BusinessesForm
from . import models
from django.db.models import F
from .models import userFavoritesBusiness

#rendering home page
def initial(request):
    return render(request, "home.html")

#dashboard view
def dashboard(request):
    if request.user.is_authenticated:
        #retrieves all the businesses in the database into this list
        allBusinesses = Businesses.objects.all
        number_range = range(1, 6)
        #the first if statement for the ratings for each business
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

            #this is to filter the businesses
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


            #this is to add a business to favorites
            elif request.POST.get("action") == "favorite":

                businessRequest = request.POST["businessName"]
                userNameRequest = request.user.username
                newEntry = userFavoritesBusiness(name = userNameRequest, business=businessRequest)
                newEntry.save()



        return render(request, "dashboard.html", {"allBusinesses": allBusinesses, "number_range": number_range})
    else:
        return redirect("home")


#add a business page
def add(request):
    if request.user.is_authenticated:
        #inputting the business entered into the database
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
            #redirects the user back to the home page if they are not logged in
            return redirect("home")

#this is for the favorites page
def favorites(request):
    needToLoadBusinesses = []
    number_range = range(1, 6)
    favoritesAll = userFavoritesBusiness.objects.filter(name=request.user.username)
    newfav = favoritesAll.values_list("business", flat=True)
    busi = Businesses.objects.all()

    favorite_businesses = Businesses.objects.filter(
        #the __ asks the orm to retrieve all the fields where the values are equal to the values in the newFav list
        name__in=newfav
    )

    print(favorite_businesses)

    return render(request, "favorites.html", {"allBusinesses": favorite_businesses, "number_range": number_range})

#this is for the coupons page
def coupons(request):
    toast=False
    if request.method == "POST":
        toast = True
    return render(request, "coupons.html", {"toast": toast})

#rendering instructions page
def instruction(request):
    answer=""
    question = ""
    if request.method == "POST":
        if request.POST.get("action") == "How do I add a business to my favorites?":
            answer = "It's quite simple! Just hit 'Learn More' for the business that you would like to add to favorites. Then, hit the 'Favorite' button under the picture! Navigate to your favorites pages, and this business should be there!"
            question = request.POST.get("action")
        elif request.POST.get("action") == "How to create a business account?":
            answer = "Contact 'customerservice@neibor.com' to get your business account created!"
            question = request.POST.get("action")
    return render(request, "instruction.html", {"answer": answer, "question": question})



def editBusinesses(request):
    allBusinesses = Businesses.objects.all

    if request.method == "POST":
        if request.POST.get("action") == "edit":
            try:
                newImage = request.POST["image"]
            except:
                newImage = ""

            try:
                newCategory = request.POST["category"]
            except:
                newCategory = ""

            try:
                newDescription = request.POST["description"]
            except:
                newDescription = ""

            try:
                newAddress = request.POST["address"]
            except:
                newAddress = ""

            BusinessName = request.POST["name"]
            print(BusinessName)
            business = get_object_or_404(Businesses, name=BusinessName)
            if newImage != "":
                business.image = newImage
            if newCategory != "":
                business.category = newCategory
            if newDescription != "":
                business.description = newDescription
            if newAddress != "":
                business.address = newAddress
            business.save()

        if request.POST.get("action") == "delete":
            BusinessName = request.POST["name"]
            print(BusinessName)
            business = get_object_or_404(Businesses, name=BusinessName)
            business.delete()
            messages.success(request, f"{BusinessName} Deleted")
            return redirect("dashboard")


    return render(request, "edit.html", {"allBusinesses": allBusinesses})




















