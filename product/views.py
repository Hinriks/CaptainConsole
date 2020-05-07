from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    context = {'products': Product.objects.all().order_by('name') }
    return render(request, 'product/index.html', context)
