from django.urls import path
from .views import brand, brand_detail, BrandGenericConcreteAPIView, BrandDetailGenericConcreteAPIView

urlpatterns = [
    path('', brand, name='api_brand'),
    path('<int:pk>/', brand_detail, name='api_brand_detail'),
    path('concrete/', BrandGenericConcreteAPIView.as_view(), name='api_brand_generic_concrete'),
    path('concrete/<int:pk>/', BrandDetailGenericConcreteAPIView.as_view(), name='api_brand_detail_generic_concrete'),
]
