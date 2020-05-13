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
        #check if product is in cart
        cartitems = user.cart.cart_item.all()
        added = False
        for cartitem in cartitems:
            if cartitem.product.id == product_id:
                cartitem.quantity += 1 #TODO her tharf ad breita hvad morg
                cartitem.save()
                added = True
                for cartitem in cartitems:
                    cart.total += cartitem.quantity * cartitem.product.price


        if not added:
            product = Product.objects.get(pk=product_id)
            cart_item = CartItem()
            cart_item.product = product
            cart_item.cart = user.cart
            cart_item.quantity = 1 #TODO her tharf ad breita hvad morg
            cart_item.line_total = cart_item.product.price * cart_item.quantity
            cart_item.save()
            for cartitem in cartitems:
                cart.total = cartitem.quantity * cartitem.product.price
        
            
    return redirect(view_cart)

def calc_total(cart):
    cartitems = cart.cart_item.all()
    for cartitem in cartitems:
        cart.total = cartitem.quantity * cartitem.product.price
    cart.save()
    


def delete_cartitem(request, id):
    cartitem = get_object_or_404(CartItem, pk=id)
    cartitem.delete()
    return redirect(view_cart)

def view_cart(request):
    try:
        username_from_request = request.user.username
        user = User.objects.get(username=username_from_request)
        cartitems = user.cart.cart_item.all()
        context = {'cartitems': cartitems}
        calc_total(user.cart)
    except:
        context = {'cartitems': 'None'}

    return render(request, 'cart/index.html', context)


def order(request):
    #TODO Setja upp þannig að það sé stage 1 og 2 af order en halda sama url. Bannaður beinn aðgangur
    return render(request, 'order/index.html')


def receipt(request, id):
    #TODO Ef "receipt.owner = user" þá kemstu á þessa síðu annars aðgangur bannaður (403)
    return render(request, 'order/receipt.html')

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
