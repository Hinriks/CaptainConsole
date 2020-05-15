from django.http import JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from user.models import User
from cart.models import CartItem, Cart

# Create your views here.


def index(request):
    return render(request, 'cart/index.html')


def add_to_cart(request, id):
    product_id = id
    if request.user.is_authenticated:
        username_from_request = request.user.username
        user = User.objects.get(username=username_from_request)

        #check if product is in cart
        cartitems = user.cart.cart_item.all()
        added = False
        for cartitem in cartitems:
            if cartitem.product.id == product_id:
                cartitem.quantity += 1 #TODO her tharf ad breita hvad morg
                cartitem.line_total = cartitem.product.price * cartitem.quantity
                cartitem.save()
                added = True
                calc_total(user.cart)


        if not added:
            product = Product.objects.get(pk=product_id)
            cart_item = CartItem()
            cart_item.product = product
            cart_item.cart = user.cart
            cart_item.quantity = 1 #TODO her tharf ad breita hvad morg
            cart_item.line_total = cart_item.product.price * cart_item.quantity
            cart_item.save()
            calc_total(user.cart)
        
            
    return redirect(view_cart)

def calc_total(cart):
    cartitems = cart.cart_item.all()
    cart.total = 0
    for cartitem in cartitems:
        cart.total += cartitem.line_total
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

def view_checkout(request):

    return render(request, 'order_summary.html')


def order(request):
    #TODO Setja upp þannig að það sé stage 1 og 2 af order en halda sama url. Bannaður beinn aðgangur
    return render(request, 'order/index.html')


def receipt(request, id):
    #TODO Ef "receipt.owner = user" þá kemstu á þessa síðu annars aðgangur bannaður (403)
    return render(request, 'order/receipt.html')
