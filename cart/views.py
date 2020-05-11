from django.http import JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from user.models import User
from cart.models import CartItem

# Create your views here.



def index(request):
    return render(request, 'cart/index.html')




def add_to_cart(request, id):
    product_id = id
    if request.user.is_authenticated:
        username_from_request = request.user.username
        user = User.objects.get(username=username_from_request)

        if not user.cart:
            new_cart = Cart()
            new_cart.user = user
            new_cart.save()

        product = Product.objects.get(pk=product_id)
        cart_item = CartItem()
        cart_item.product = product
        cart_item.cart = user.cart
        cart_item.quantity = 1
        cart_item.line_total = cart_item.product.price * cart_item.quantity
        cart_item.save()
            
    return render(request, 'cart/index.html')

def view_cart(request):
    username_from_request = request.user.username
    user = User.objects.get(username=username_from_request)
    cartitems = user.cart.cart_item.all()
    print(cartitems)
    context = {'cartitems': cartitems}
    print(context)
    return render(request, 'cart/index.html', context)





"""
    username_from_request = request.user.username
    user = User.objects.get(username=username_from_request)
    cart = user.cart
    context = {'cart': }
    return render(request, 'product/index.html', context)
 """
            







    #TODO ALLT HEHE
"""
    #Virkar ekki shit
    if request.GET:
        pass
    if request.POST:
        user = request.logged_in_user
        if user.cart:
            cart_item = CartItem()
        else:
            cart1 = Cart()
            cart_item1 = CartItem()
            cart1.user = user
            cart_item1.cart = cart1
            .
            .
            cart1.save()
"""
