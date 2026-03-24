from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/', views.restaurant_detail, name='restaurant_detail'),
]