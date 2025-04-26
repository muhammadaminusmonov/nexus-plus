from django.urls import path, include
from .views import region, region_detail, RegionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', RegionViewSet)

urlpatterns = [
    path('', region, name='api_region'),
    path('<int:pk>/', region_detail, name='api_region_detail'),
    path('viewset/', include(router.urls)),
]