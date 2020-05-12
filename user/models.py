from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address = models.CharField(max_length=100, blank=True )
    #date_of_birth = models.TextField()

