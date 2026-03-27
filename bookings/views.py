from django.shortcuts import render
from .models import Restaurant
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required



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
            booking.user = request.user 
            booking.save()
            messages.success(request, "Your booking has been created!")
            return redirect('home')
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been updated!")
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})