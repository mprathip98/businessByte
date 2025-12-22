from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def initial(request):
    if request.user.is_authenticated:
        userFirstName = request.user.get_short_name()

        return render(request, "home.html", {"fname":userFirstName})
    else:
        return render(request, "home.html")

