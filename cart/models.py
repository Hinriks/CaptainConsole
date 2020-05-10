from django.db import models
from product.models import Product

# Create your models here.
class CartItem(models.Model):
    product = models.ManyToManyField("Product", on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.product.name


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, null=True, blank=True)
    total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.id
    