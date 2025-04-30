from django.urls import path, include
from .views import region, region_detail, RegionViewSet, RegionConcrete, RegionDetailConcrete
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', RegionViewSet)

urlpatterns = [
    path('', region, name='api_region'),
    path('<int:pk>/', region_detail, name='api_region_detail'),
    path('viewset/', include(router.urls), name='api_region_viewset'),
    path('concrete/', RegionConcrete.as_view(), name='api_region_concrete'),
    path('concrete/<int:pk>/', RegionDetailConcrete.as_view(), name='api_region_detail_concrete'),
]