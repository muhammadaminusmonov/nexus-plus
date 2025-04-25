from django.urls import path
from .views import BlogView, BlogDetailView, BlogGenericView, BlogDetailGenericView, BlogGenericMixinsView, BlogDetailGenericMixinView

urlpatterns = [
    path('', BlogView.as_view(), name='api_blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name='api_blog_detail'),
    path('generic/', BlogGenericView.as_view(), name='api_blog_generic'),
    path('generic/<int:pk>/', BlogDetailGenericView.as_view(), name='api_blog_detail_generic'),
    path('mixin/', BlogGenericMixinsView.as_view(), name='api_blog_mixin'),
    path('mixin/<int:pk>/', BlogDetailGenericMixinView.as_view(), name='api_blog_detail_mixin'),
]