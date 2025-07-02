from django.contrib import admin
from .models import CustomUser, Customer, ServiceProvider, Profile
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(ServiceProvider)
admin.site.register(Profile)
