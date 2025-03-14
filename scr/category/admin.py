from django.contrib import admin
from .models import Category, Brand

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status', 'parent')

admin.site.register(Brand)