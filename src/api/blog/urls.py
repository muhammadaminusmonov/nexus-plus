from django.urls import path
from .views import BlogView, BlogDetailView

urlpatterns = [
    path('', BlogView.as_view(), name='api_blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name='api_blog_detail'),
]