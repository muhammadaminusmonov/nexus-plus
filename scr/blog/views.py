from django.shortcuts import render
from .models import Blog

def blogs(request):
    blogs = Blog.objects.order_by('-created_at')[:6].select_related('user')
    ctx = {
        'blogs': blogs,
    }
    return render(request, 'blogs.html', ctx)