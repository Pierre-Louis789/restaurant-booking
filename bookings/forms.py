from django import forms
from .models import Booking, Table
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['restaurant', 'table', 'date', 'time', 'party_size', 'special_requests']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'restaurant' in self.data:
            try:
                restaurant_id = int(self.data.get('restaurant'))
                self.fields['table'].queryset = Table.objects.filter(restaurant_id=restaurant_id)
            except (ValueError, TypeError):
                self.fields['table'].queryset = Table.objects.none()
        else:
            self.fields['table'].queryset = Table.objects.none()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
