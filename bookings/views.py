from django.shortcuts import render
from .models import Restaurant
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')

def restaurant_detail(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # assign logged-in user
            booking.save()
            messages.success(request, "Your booking has been created!")
            return redirect('home')
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form})
