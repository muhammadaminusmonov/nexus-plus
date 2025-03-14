from django.contrib import admin
from .models import Product, ProductImage, Discount, ProductView


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Discount)