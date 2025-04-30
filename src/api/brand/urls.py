from django.urls import path, include
from .views import brand, brand_detail, BrandGenericConcreteAPIView, BrandDetailGenericConcreteAPIView, BrandViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BrandViewSet)

urlpatterns = [
    path('', brand, name='api_brand'),
    path('<int:pk>/', brand_detail, name='api_brand_detail'),
    path('concrete/', BrandGenericConcreteAPIView.as_view(), name='api_brand_generic_concrete'),
    path('concrete/<int:pk>/', BrandDetailGenericConcreteAPIView.as_view(), name='api_brand_detail_generic_concrete'),
    path('viewset/', include(router.urls), name='api_brand_viewset'),
]
