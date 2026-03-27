from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/', views.restaurant_detail, name='restaurant_detail'),
    path('book/', views.create_booking, name='create_booking'),
]