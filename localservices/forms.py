from .models import Bookings
from django import forms

class BookingForm(forms.ModelForm):
	class Meta:
		model = Bookings
		fields = ['customer', 'provider', 'preferred_date', 'preferred_time', 'urgency_level', 'additional_notes']
