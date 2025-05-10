from rest_framework import status, viewsets
from rest_framework.response import Response
from api.region.serializers import RegionSerializer
from region.models import Region
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

@api_view(['GET', 'POST'])
def region(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail": f"Method '{request.method}' not allowed "}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def region_detail(request, pk):
    try:
        region = Region.objects.get(pk=pk)
    except Region.DoesNotExist:
        return Response({"error": "region not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = RegionSerializer(region, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({"detail": f"Method '{request.method}' not allowed "}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RegionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionConcrete(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailConcrete(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer