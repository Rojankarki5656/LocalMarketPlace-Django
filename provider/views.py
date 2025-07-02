from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from localservices.models import Bookings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView

@login_required
def provider_dashboard(request):
    if request.user.role == 'provider' and request.user.is_authenticated:
        pending_bookings = Bookings.objects.filter(provider=request.user, status='pending').count()
        customers = Bookings.objects.filter(provider=request.user).count()
        bookings = Bookings.objects.filter(provider=request.user)
        return render(request, 'provider/provider-dashboard.html', {
            'pending_bookings': pending_bookings,
            'total_clients': customers,
            'bookings': bookings
            })

class UpdateBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bookings
    template_name = 'provider/update-booking.html'
    fields = ['status']
    success_url = '/'

    def form_valid(self, form):
        form.instance.provider = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.provider:
            return True
        return False