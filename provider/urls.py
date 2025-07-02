from django.urls import path
from . import views

urlpatterns = [
    path('provider-dashboard/', views.provider_dashboard, name='provider-dashboard'),
    path('update/<int:pk>', views.UpdateBooking.as_view(), name='update-booking'),
    ]
