from django.db import models
from user.models import Profile
from category.models import Category

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="replies")

    def __str__(self):
        return self.user.user
