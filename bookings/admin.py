from django.contrib import admin
from .models import Restaurant, Table, Booking, Profile

admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'date', 'time', 'party_size', 'status')
    list_filter = ('status', 'restaurant')
    list_editable = ('status',)

admin.site.register(Profile)