from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from product.forms.product_form import ProductCreateForm, ProductUpdateForm
from product.models import Product, ProductImage, Promo, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import random


# Create your views here.
def homepage(request):
    loginform = AuthenticationForm()
    random_products = get_popular_products()
    featured_products = get_featured_products()
    user = get_user(request)
    promos = get_promos()
    cats = get_menu()
    context = {'popular_products': random_products, 'featured_products': featured_products, 'promos': promos, 'user': user, 'loginform':loginform, 'cats': cats}
    return render(request, 'home/index.html', context)


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({ 'data': products })
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)

def get_popular_products():
    """ Get random 4 products to display in Popular Products """
    products = list(Product.objects.all())
    random_products = random.sample(products, 4)
    return random_products

def get_featured_products():
    """ Get first 4 products from featured category """
    products = list(Product.objects.filter(featured=True))
    featured_products = products[:4]
    return featured_products

def get_promos():
    promos = Promo.objects.all().filter(active=True)
    return promos


def get_menu():
    cats = Category.objects.all()
    return cats



# /product/3
def get_product_by_id(request, id):
    context = {'product': get_object_or_404(Product, pk=id)}
    return render(request, 'product/product_details.html',context)


def create_product(request):
    user = get_user(request)
    if user.is_staff:
        if request.method == 'POST':
            form = ProductCreateForm(data=request.POST)
            if form.is_valid():
                product = form.save()
                product_image = ProductImage(image=request.POST['image'], product=product)
                product_image.save()
                return redirect('product-index')
        else:
            form = ProductCreateForm()
        return render(request, 'product/create_product.html', {
            'form': form
        })


def delete_product(request, id):
    user = get_user(request)
    if user.is_staff:
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect('product-index')


def update_product(request, id):
    user = get_user(request)
    if user.is_staff:        
        instance = get_object_or_404(Product, pk=id)
        if request.method == 'POST':
            form = ProductUpdateForm(data=request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('product-details', id=id)
        else:
            form = ProductUpdateForm(instance=instance)
        return render(request, 'product/update_product.html', {
            'form': form,
            'id': id
        })


def get_user(request):
    user = request.user
    return user
