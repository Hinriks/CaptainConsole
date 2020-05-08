from django.shortcuts import render, get_object_or_404
from product.models import Product


# Create your views here.
def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)


# /product/3
def get_product_by_id(request, id):
    context = {'product': get_object_or_404(Product, pk=id)}
    return render(request, 'product/product_details.html',context)


