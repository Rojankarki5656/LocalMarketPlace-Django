from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bookings
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import BookingForm
from users.models import Customer, ServiceProvider
from django.views.generic import ListView, DetailView,  DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def home(request):
	return render(request, 'localservices/index.html')

class ProviderListView(ListView):
	model = ServiceProvider
	template_name = 'localservices/services.html'
	context_object_name = 'providers'


def contact(request):
	return render(request, 'localservices/contact.html')

def createBooking(request, pk):
	object = get_object_or_404(ServiceProvider, pk=pk)
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f"Booking Confirmed")
	else:
		form = BookingForm()
	return render(request, 'localservices/booking.html', {'object': object, 'form': form})

class ProviderDetailView(DetailView):
	model = ServiceProvider
	template_name = 'localservices/service-detail.html'

def profile(request):
	return render(request, 'users/profile.html')


def booking_details(request, pk):
	booking_details = get_object_or_404(Bookings, pk=pk)
	return render(request, 'localservices/booking-details.html', {'booking': booking_details})


class DeleteBooking(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
	model = Bookings
	template_name = 'localservices/cancel-booking.html'
	success_url = reverse_lazy('dashboard')

	def test_func(self):
		book = self.get_object()
		if self.request.user == book.customer:
			return True
		return False