from django.urls import path
from . import views

urlpatterns = [
	path('messages/', views.user_messages, name='messages')
]