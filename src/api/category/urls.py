from django.urls import path
from .views import category, category_detail

urlpatterns = [
    path('', category, name='api_category'),
    path('<int:pk>/', category_detail, name='api_category_detail'),
]