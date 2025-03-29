from django.urls import path
from .views import product_list, product_detail, product_add

urlpatterns = [
    path("", product_list, name="products"),
    path('<int:pk>/<slug:slug>', product_detail, name="product_detail"),
    path('product_add', product_add, name='product_add'),
]