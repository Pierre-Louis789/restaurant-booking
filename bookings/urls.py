from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.create_booking, name='create_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]