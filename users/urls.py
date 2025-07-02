from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('update/profile/', views.edit_profile, name='update-profile'),
    path('update/info/<int:pk>/', views.UpdateInfo.as_view(), name='update-info'),
    path('upadate/business/<int:pk>/', views.UpdateProviderPersonalInfo.as_view(), name='update-business')
]
