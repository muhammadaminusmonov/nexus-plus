from django.urls import path
from .views import region, region_detail

urlpatterns = [
    path('', region, name='api_region'),
    path('<int:pk>/', region_detail, name='api_region_detail'),
]