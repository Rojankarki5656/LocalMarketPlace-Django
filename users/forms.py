from .models import CustomUser, Customer, ServiceProvider, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'first_name', 'last_name','email', 'phone', 'role']

class CustomerRegisterForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['address', 'city', 'state', 'zip_code']

class ProviderRegisterForm(forms.ModelForm):
	class Meta:
		model = ServiceProvider
		fields = ['business_name', 'category', 'experience', 'hourly_rate', 'service_area', 'business_description']

class ProfileUpdate(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']