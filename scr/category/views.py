from django.shortcuts import render
from region.models import Region
from category.models import Category
from django.db.models import Count, Sum
from product.models import Product

def categories_page(request):
    regions = Region.objects.all()
    categories = Category.objects.filter(parent=None)
    count_products = Category.objects.aggregate(Count('product'))
    category_count_product = (
        Category.objects
        .filter(parent=None)
        .annotate(count_product=Count('product') + Sum('category__product'))
    )
    products = (
        Product.objects
        .filter(status=1)
        .order_by('-created_at')[:12]
        .select_related('category', 'location', 'brand', 'user', 'discount')
        .prefetch_related('images')
    )

    ctx = {
        "regions": regions,
        "categories": categories,
        "count_products": count_products,
        "category_count_product": category_count_product,
        "products": products,
    }
    return render(request, 'category.html', ctx)