from django.urls import path
from . import views
from django.conf import settings # Import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.initial, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("add/", views.add, name="add"),
]