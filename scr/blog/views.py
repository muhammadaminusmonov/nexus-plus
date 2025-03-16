from django.db.models import Count
from django.shortcuts import render
from category.models import Category
from .models import Blog
from django.core.paginator import Paginator


def blogs(request):
    all_blogs = (
        Blog.objects
        .order_by('-created_at')
        .select_related('user', 'category')
        .annotate(
            comment_count=Count('comments') + Count('comments__replies')
        )
    )
    paginator = Paginator(all_blogs, 1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    categories = (
        Category.objects
        .filter(status=2)
        .annotate(
            category_count=Count('blog', distinct=True)+Count('children__blog', distinct=True)
        )
    )

    recent_blogs = Blog.objects.order_by('-created_at')[:5]

    ctx = {
        'blogs': page_obj,
        'categories': categories,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'blogs.html', ctx)