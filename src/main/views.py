from django.shortcuts import render
from category.models import Category
from region.models import Region
from product.models import Product, ProductImage
from django.db.models import Count, Prefetch
from blog.models import Blog
from category.models import Category
from .forms import EmailForm
from django.core.mail import send_mail

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

def about_page(request):
    ctx = {}
    return render(request, 'about.html', ctx)

def services_page(request):
    ctx = {}
    return render(request, 'services.html', ctx)

def contact_page(request):
    form = EmailForm()
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["muhammadamincoder@gmail.com"],
        fail_silently=False,
    )
    ctx = {
        "form": form
    }
    return render(request, 'contact.html', ctx)