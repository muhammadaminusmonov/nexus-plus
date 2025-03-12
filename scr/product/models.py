from django.db import models
from user.models import Profile
from category.models import Category, Brand
from region.models import Region


class Product(models.Model):
    condition_types = [
        (1, "New"),
        (2, "Used"),
        (3, "Unpacked")
    ]

    status_types = [
        (1, "ACTIVE"),
        (2, "INACTIVE"),
        (3, "SOLD")
    ]
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    condition = models.SmallIntegerField(choices=condition_types, default=1)
    status = models.SmallIntegerField(choices=status_types, default=1)
    price = models.IntegerField(null=True, blank=True)
    price_on_call = models.BooleanField(default=False)
    slug = models.SlugField()
    featured = models.BooleanField(default=False)
    review = models.ForeignKey('ProductReview', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProductView(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='')
    is_main = models.BooleanField(default=False)

class ProductReview(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    review = models.TextField(null=False, blank=False)
    rating = models.SmallIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.user} - {self.products}"


class Discount(models.Model):
    status_types = [
        (1, "ACTIVE"),
        (2, "INACTIVE")
    ]
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    percentage = models.SmallIntegerField(null=False, blank=False)
    status = models.SmallIntegerField(choices=status_types, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.percentage}% off"
