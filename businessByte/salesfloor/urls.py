from django.urls import path
from . import views
from django.conf import settings # Import settings
from django.conf.urls.static import static


#for navigating into each page
urlpatterns = [
    path('', views.initial, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("add/", views.add, name="add"),
    path("favorites/", views.favorites, name="favorites"),
    path("coupons/", views.coupons, name="coupons"),
    path("instruction/", views.instruction, name="instruction"),
    path("edit/", views.editBusinesses, name="edit")
]

#to render pictures for each business
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)