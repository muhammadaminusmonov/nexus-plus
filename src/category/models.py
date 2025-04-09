from django.db import models

class Category(models.Model):
    STATUS_CHOICES = [
        (1, "PRODUCT"),
        (2, "BLOG"),
    ]
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='')
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name
