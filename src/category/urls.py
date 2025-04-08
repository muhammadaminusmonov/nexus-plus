from django.urls import path
from .views import category_form

urlpatterns = [
    path('', category_form, name='category_form'),
]