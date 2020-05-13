from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999, blank=True)
    year_of_start = models.DateTimeField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    def __str__(self):
        if self.parent_category:
            return "{} > {}".format(self.parent_category, self.name)
        else:
            return self.name

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

class Promo(models.Model):
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    image = models.CharField(max_length=999)
    active = models.BooleanField(default=False)
    def __str__(self):
        return "{} Promo - Active:{}".format(self.product.name,self.active)
    