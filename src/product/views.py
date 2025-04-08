from django.shortcuts import render, redirect
from region.models import Region
from category.models import Category
from django.db.models import Count, Prefetch
from product.models import Product, ProductImage
from user.models import Profile
from django.core.paginator import Paginator
from .forms import AddProductForm
from django.contrib.auth.models import User

def product_list(request):
    regions = Region.objects.all()
    categories = (
        Category.objects
        .filter(parent=None, status=1)
        .annotate(
            product_count=Count('product', distinct=True) + Count('children__product', distinct=True)
        )
    )
    products = (
        Product.objects
        .filter(status=1)
        .order_by('-created_at')
        .select_related('category', 'location', 'brand', 'user', 'discount')
        .prefetch_related('images')
    )

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    ctx = {
        "regions": regions,
        "categories": categories,
        "page_obj": page_obj,
        "total_products": products.count,
        "page_range": paginator.page_range,
        "page_number": page_number,
    }
    return render(request, 'products.html', ctx)

def product_detail(request, pk, slug=None):
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

def product_add(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user.profile
            product.save()
            return redirect('home')
    else:
        form = AddProductForm()

    ctx = {
        "user": user,
        "profile": profile,
        "form": form,
    }
    return render(request, 'product_add.html', ctx)