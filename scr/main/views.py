from django.shortcuts import render
from category.models import Category
from region.models import Region
from product.models import Product, ProductImage
from django.db.models import Count, Prefetch
from blog.models import Blog


def home_page(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = (
        Product.objects
        .order_by('-created_at')[:6]
        .select_related('category', 'location', 'brand', 'user')
        .prefetch_related(Prefetch('images', queryset=ProductImage.objects.filter(is_main=True)))
    )
    featured_products = (
        Product.objects
        .filter(featured=True)
        .select_related("category", "location", "review")
        .prefetch_related(Prefetch("images", queryset=ProductImage.objects.filter(is_main=True)))
        .annotate(review_count=Count("review"))
    )

    blogs = Blog.objects.order_by('-created_at')[:3].select_related("user")

    ctx = {
        "categories": categories,
        "regions": regions,
        "products": products,
        "featured_products": featured_products,
        "blogs": blogs,
    }
    return render(request, 'index.html', ctx)