from django.shortcuts import render
from .models import Restaurant
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')

def restaurant_detail(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, id):
    restaurant = Restaurant.objects.get(id=id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            messages.success(request, "Registration successful! Welcome.")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def custom_logout(request):
    logout(request)  # fully clears ALL sessions
    return redirect('home')


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

@login_required
def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Your booking has been cancelled.")
        return redirect('my_bookings')

    return render(request, 'delete_booking.html', {'booking': booking})

@login_required
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    return render(request, 'booking_confirmation.html', {'booking': booking})


@login_required
def create_booking(request):
    restaurants = Restaurant.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Your booking has been created!")
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {
        'form': form,
        'restaurants': restaurants
    })