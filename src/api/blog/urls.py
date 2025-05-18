from django.urls import path, include
from .views import (
    BlogView,
    BlogDetailView,
    BlogGenericView,
    BlogDetailGenericView,
    BlogGenericMixinsView,
    BlogDetailGenericMixinView,
    BlogViewSet,
    BlogConcrete,
    BlogDetailConcrete
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BlogViewSet)

urlpatterns = [
    path('', BlogView.as_view(), name='api_blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name='api_blog_detail'),
    path('generic/', BlogGenericView.as_view(), name='api_blog_generic'),
    path('generic/<int:pk>/', BlogDetailGenericView.as_view(), name='api_blog_detail_generic'),
    path('mixin/', BlogGenericMixinsView.as_view(), name='api_blog_mixin'),
    path('mixin/<int:pk>/', BlogDetailGenericMixinView.as_view(), name='api_blog_detail_mixin'),
    path('viewset/', include(router.urls), name='api_blog_viewset'),
    path('concrete/', BlogConcrete.as_view(), name='api_blog_concrete'),
    path('concrete/<int:pk>/', BlogDetailConcrete.as_view(), name='api_blog_detail_concrete'),
]