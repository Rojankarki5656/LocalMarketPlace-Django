from django.contrib.auth import authenticate, login
from .models import CustomUser, Customer, Profile, ServiceProvider
from localservices.models import Bookings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, CustomerRegisterForm, ProviderRegisterForm, ProfileUpdate
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('username')  # could be email or username
        password = request.POST.get('password')

        # Try to authenticate directly with username
        customer = CustomUser.objects.all().filter(username=identifier, password=password)
        print(customer)
        user = authenticate(request, username=identifier, password=password)

        # If not found, try by email
        if user is None:
            try:
                user_obj = CustomUser.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except CustomUser.DoesNotExist:
                user = None

        # Final check
        if user is not None:
            login(request, user)  # ✅ this sets the session cookie
            # Redirect based on role
            if user.role == 'customer':
                return redirect('dashboard')
            elif user.role == 'provider':
                return redirect('provider-dashboard')
        else:
            messages.error(request, "Invalid username/email or password.")

    return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            role = form.cleaned_data.get("role")
            user = form.save(commit=False)
            user.save()
            if role == 'customer':
                customerform = CustomerRegisterForm(request.POST)
                if customerform.is_valid():
                    customer = customerform.save(commit=False)
                    customer.user = user
                    customer.save()
                    messages.success(request, f"Customer account created for {username}")
                    return redirect('dashboard')
            elif role == 'provider':
                providerform = ProviderRegisterForm(request.POST)
                print(request.POST)
                print(providerform)
                if providerform.is_valid():
                    provider = providerform.save(commit=False)
                    provider.user = user
                    provider.save()
                    messages.success(request, f"Provider account created for {username}")
                    return redirect('provider-dashboard')

        # If profile form is invalid (fallback)
        messages.error(request, "Something went wrong. Please check your inputs.")

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def user_dashboard(request):
    if request.user.role == 'customer' and request.user.is_authenticated:
        pending_bookings = Bookings.objects.filter(customer=request.user, status='pending').count()
        completed_bookings = Bookings.objects.filter(customer=request.user, status='completed').count()
        bookings = Bookings.objects.filter(customer=request.user)
        return render(request, 'localservices/user-dashboard.html', {
            'bookings': bookings,
            'pending_bookings': pending_bookings,
            'completed_bookings': completed_bookings
            })
    elif request.user.role == 'provider' and request.user.is_authenticated:
        return render(request, 'provider/provider-dashboard.html')

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdate
    return render(request, 'users/edit-profile.html', {'title': 'Profile', 'form': form})

class UpdateInfo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'users/edit-profile.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        print(self.request.user.id, post.id)
        if self.request.user.id == post.id:
            return True
        return False


class UpdatePersonalInfo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Customer
    template_name = 'users/edit-profile.html'
    fields = ['address', 'zip_code', 'city', 'state']
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        print(self.request.user.id, post.id)
        if self.request.user.id == post.id:
            return True
        return False

class UpdateProviderPersonalInfo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ServiceProvider
    template_name = 'users/edit-profile.html'
    fields = ['business_name', 'category', 'experience', 'hourly_rate', 'service_area', 'business_description']
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        print(self.request.user.id, post.id)
        if self.request.user.id == post.id:
            return True
        return False