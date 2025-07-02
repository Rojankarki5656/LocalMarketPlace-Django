from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('services/', views.ProviderListView.as_view(), name = 'services'),
    path('contact/', views.contact, name = 'contact'),
    path('booking/<int:pk>/', views.createBooking, name = 'booking'),
    path('services-details/<int:pk>/', views.ProviderDetailView.as_view(), name="service-detail"),
    path('profile/', views.profile, name='profile'),
    path('booking-details/<int:pk>/', views.booking_details, name = 'booking-details'),
    path('cancel-bookings/<int:pk>/', views.DeleteBooking.as_view(), name = 'cancel-booking')
]