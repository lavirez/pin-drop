from django.db import models
from django.contrib.auth import AbstractUser

# def profile_img_upload(instance, filename):


class User(AbstractUser):
	phone_number = models.CharField(max_length=20, blank=True)
	profile_photo = models.ImageField(upload_to=profile_img_upload)
	pioneer_point = models.PositiveIntegerField(default=0)
	is_leader = models.BooleanField(default=False)

	def __str__(self):
		return self.username