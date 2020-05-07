from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999, blank=True)
    year_of_start = models.DateTimeField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    # Name, Images, Description, Price, Manufacturer, Inventory, Hidden
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

