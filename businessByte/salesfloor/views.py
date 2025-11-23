from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def initial(request):
    return HttpResponse('Initial Page')