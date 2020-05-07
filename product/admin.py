from django.contrib import admin

# Register your models here.
from .models import Manufacturer, Product, ProductImage, Category

admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)