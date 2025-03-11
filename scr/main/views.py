from django.shortcuts import render
from category.models import Category
from region.models import Region
from product.models import Product
from django.db.models import Count

def home_page(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = (
        Product.objects
        .filter(status=1)
        .order_by('-created_at')[:6]
        .select_related('category', 'location', 'brand', 'user')
        .prefetch_related('images')
    )
    featured_products = (
        Product.objects
        .filter(is_featured=True)
        .select_related("review", "category", "location")
        .prefetch_related("images")
        .annotate(review_count=Count("review"))
    )

    ctx = {
        "categories": categories,
        "regions": regions,
        "product": products,
        "featured_products": featured_products,
    }
    return render(request, 'index.html', ctx)