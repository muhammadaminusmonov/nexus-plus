from django.urls import path, include
from .views import category, category_detail, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CategoryViewSet)

urlpatterns = [
    path('', category, name='api_category'),
    path('<int:pk>/', category_detail, name='api_category_detail'),
    path('viewset/', include(router.urls), name='api_category_viewset'),
]
