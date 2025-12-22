from django.urls import path
from . import views

urlpatterns = [
    path('', views.initial, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("add/", views.add, name="add"),
]