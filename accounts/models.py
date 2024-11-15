from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomCompany(AbstractUser):
	company = models.CharField(max_length=128, unique=True)
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.company