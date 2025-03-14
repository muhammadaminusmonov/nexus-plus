from django.shortcuts import render
from region.models import Region
from category.models import Category
from django.db.models import Count, Sum, Prefetch
from product.models import Product, ProductImage
from user.models import Profile

def product_list(request):
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
    return render(request, 'products.html', ctx)

def product_detail(request, pk):
    product = (
        Product.objects
        .select_related('category', 'location', 'brand', 'user', 'discount', 'review')
        .prefetch_related('images')
        .get(pk=pk)
    )
    posted_by = Profile.objects.get(pk=product.user.pk)
    products_by_seller = (
        Product.objects
        .filter(user=product.user)
        .select_related('location', 'brand', 'user')
        .prefetch_related(Prefetch('images', queryset=ProductImage.objects.filter(is_main=True)))
    )
    ctx = {
        "product": product,
        "posted_by": posted_by,
        "products_by_seller": products_by_seller,
    }
    return render(request, 'product_detail.html', ctx)