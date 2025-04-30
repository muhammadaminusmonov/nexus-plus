from rest_framework.serializers import ModelSerializer
from blog.models import Blog, BlogComment


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        exclude = ['created_at', 'slug']

class BlogCommentSerializer(ModelSerializer):

    class Meta:
        model = BlogComment
