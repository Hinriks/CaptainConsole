import random
from product.models import Product
from django import template

register = template.Library()

@register.simple_tag(name='get_popular_products')
def get_popular_products():
    """ Get random 4 products to display in Popular Products """
    products = Product.objects.all()
    random_products = random.sample(products, 4)
    return random_products
