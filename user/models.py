import datetime
from cart.models import Cart
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

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

User._meta.get_field('username').validators[1].limit_value = 15
User._meta.get_field('username').max_length = 15
User._meta.get_field('username').help_text = ('Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.')

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    apt = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    card_name = models.CharField(max_length=150)
    card_number = models.CharField(max_length=16)
    card_cvc = models.CharField(max_length=3)
    card_exp_month = models.CharField(max_length=2)
    card_exp_year = models.CharField(max_length=4)


    def __str__(self):
        return '{} - {}'.format(1, self.id)


@receiver(post_save, sender=Order)
def remove_user_from_cart(sender, instance, created, **kwargs):
    if not created:
        user_i = instance.cart.user
        cart = user_i.cart
        cart.user = None
        user_i.cart = Cart()
        cart.save()
        user_i.cart.save()