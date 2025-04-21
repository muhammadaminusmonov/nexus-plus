from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from category.models import Category


@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True).data
        return Response(result, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        categories = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        result = CategorySerializer(categories).data
        return Response(result, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = CategorySerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
