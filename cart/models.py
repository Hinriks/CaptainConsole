from django.db import models
from product.models import Product
from django.conf import settings


# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
        related_name='cart_item'
    )
    quantity = models.IntegerField(default=1)
    line_total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "ID: {} - {} Owner:{}".format(self.id, self.product.name, self.cart.user)


class Cart(models.Model):
    # items = models.ManyToManyField(CartItem, blank=True)
    total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True, related_name='cart')

    def __str__(self):
        return "{} Cart".format(self.user)
     