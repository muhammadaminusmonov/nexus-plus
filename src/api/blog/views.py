from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from blog.models import Blog
from .serializers import BlogSerializer

class BlogView(APIView):
    def get(self, request):
        blogs = Blog.objects.order_by('-updated_at')

        paginator = PageNumberPagination()
        paginator.page_size = 3
        result_page = paginator.paginate_queryset(blogs, request)

        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):

    def get_object(self, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        return blog

    def get(self, request, pk):
        blog = self.get_object(pk=pk)
        serializer = BlogSerializer(blog).data
        return Response(serializer, status=status.HTTP_200_OK)

    def put(self, request, pk):
        blog = self.get_object(pk=pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)