from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from .forms import Memberform
from django.contrib import messages


def say_hello(request):
    allMembers = Member.objects.all
    return render(request, 'hello.html', {'all':allMembers})

def join(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("Your form has been submitted"))
        return redirect('hello')

    else:
        return render(request, 'join.html', {})