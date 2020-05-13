import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar1 = 'https://api.adorable.io/avatars/200/abytt@adorable.png'
    avatar2 = 'https://api.adorable.io/avatars/200/bbytt@adorable.png'
    avatar3 = 'https://api.adorable.io/avatars/200/cbytt@adorable.png'
    avatar4 = 'https://api.adorable.io/avatars/200/dbytt@adorable.png'
    avatar5 = 'https://api.adorable.io/avatars/200/ebytt@adorable.png'
    avatar_choices = (
        (avatar1, 'Avatar 1'),
        (avatar2, 'Avatar 2'),
        (avatar3, 'Avatar 3'),
        (avatar4, 'Avatar 4'),
        (avatar5, 'Avatar 5'),
    )
    avatar_img = models.CharField(max_length=255, choices=avatar_choices, default=avatar1)
    address = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(default=datetime.date.today, blank=True)
    phone_number = models.CharField(max_length=8, blank=True)

