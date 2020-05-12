from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="cart-index"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('order/', views.order, name="order"),
    path('order/<int:id>', views.receipt, name="receipt"),
    path('delete_cartitem/<int:id>', views.delete_cartitem, name="delete_cartitem")
]
