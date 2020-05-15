from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('product/', views.index, name="product-index"),
    path('product/<int:id>', views.get_product_by_id, name='product-details'),
    path('product/create_product', views.create_product, name="create_product"),
    path('product/delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('product/update_product/<int:id>', views.update_product, name="update_product"),
    path('product/search/<str:name>', views.view_search, name="view_search"),
]
# TODO All products page?
