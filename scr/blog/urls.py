from django.urls import path
from .views import blogs, blog_detail

urlpatterns = [
    path('', blogs, name='blogs'),
    path('<int:pk>/<slug:slug>', blog_detail, name='blog_detail')
]