from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello, name="hello"),
    path("join/", views.join, name="join"),
]