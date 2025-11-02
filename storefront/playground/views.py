from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.
def say_hello(request):
    allMembers = Member.objects.all
    print(allMembers)
    return render(request, 'hello.html', {'all':allMembers})

def join(request):
    return render(request, 'join.html', {})