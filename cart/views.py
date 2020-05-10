from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product

# Create your views here.



def index(request):
    return render(request, 'cart/index.html')


def add_to_cart(request, id):
    #Virkar ekki shit
    product = {'product': get_object_or_404(Product, pk=id)}
    request.session['cart'] = {}
    request.session['cart'] = product

    return redirect('product-details', id=id)
