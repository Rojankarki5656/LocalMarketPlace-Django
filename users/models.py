from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Create your models here.
# (zip-code, address, phone,, city, state)
class CustomUser(AbstractUser):
	phone = models.CharField(max_length = 20)	
	role = models.CharField(max_length=20)

	def __str__(self):
		return self.username

class ServiceProvider(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	business_name = models.TextField(max_length=100)
	category= models.CharField(max_length=50)
	experience = models.CharField(max_length=50)
	hourly_rate = models.CharField(max_length=10)
	service_area = models.TextField()
	business_description = models.TextField()

class Customer(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	address = models.TextField()
	zip_code = models.CharField(max_length=15, blank=True)
	city = models.CharField(max_length=30, blank=True)
	state = models.CharField(max_length=30, blank=True)

class Profile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)