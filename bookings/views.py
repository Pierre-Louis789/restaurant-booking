from django.shortcuts import render
from .models import Restaurant

def home(request):
    return render(request, 'home.html')

def restaurant_detail(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})git add .