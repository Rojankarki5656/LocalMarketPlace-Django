from django.db import models
from users.models import CustomUser
from django.utils import timezone
# Create your models here.
class Bookings(models.Model):
	customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings_made', default=0)
	provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings_received', default=0)
	status = models.CharField(max_length=50, default='pending')
	preferred_date = models.DateField(default=timezone.now)
	preferred_time = models.CharField(blank=True, max_length=50)
	urgency_level = models.CharField(max_length=50, default='Normal')
	additional_notes = models.TextField(default='')