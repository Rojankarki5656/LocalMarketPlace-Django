from django.db.models.signals import post_save
from .models import CustomUser
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=CustomUser)
def create_profile(sender, created, instance, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()