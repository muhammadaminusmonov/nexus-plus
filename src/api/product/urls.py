from django.urls import path
from .views import products

urlpatterns = [
    path('', products, name='api_products'),
]