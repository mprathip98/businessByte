from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from .forms import Memberform


def say_hello(request):
    allMembers = Member.objects.all
    return render(request, 'hello.html', {'all':allMembers})

def join(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "join.html", {})

    else:
        return render(request, 'join.html', {})