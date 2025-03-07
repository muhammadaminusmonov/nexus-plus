from django.shortcuts import render
from category.models import Category

def home_page(request):
    categories = Category.objects.filter(is_main=True)
    ctx = {
        "categories": categories
    }
    return render(request, 'index.html', ctx)