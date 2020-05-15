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
    path('product/sort/<str:sort>/<int:order>', views.view_sort, name="view_sort"),
    path('product/catagory/<int:id>', views.view_catagory, name="view_catagory"),

]
# TODO All products page?
