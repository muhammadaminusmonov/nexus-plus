from django.urls import path
from .views import brand, brand_detail

urlpatterns = [
    path('', brand, name='api_brand'),
    path('<int:pk>/', brand_detail, name='api_brand_detail'),
]
