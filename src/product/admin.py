from django.contrib import admin
from .models import Product, ProductImage, Discount

# Inline for ProductImage
class ProductImageInline(admin.TabularInline):  # or admin.StackedInline for a different style
    model = ProductImage
    extra = 1  # Number of empty forms to display

# Inline for Discount
class DiscountInline(admin.StackedInline):
    model = Discount
    extra = 1

# Customizing Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', 'featured', 'created_at']
    list_filter = ['status', 'category', 'featured']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title
    inlines = [ProductImageInline, DiscountInline]  # Add Image and Discount inline
