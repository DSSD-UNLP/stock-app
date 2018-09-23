from stockProject.stockApp.models import Product, Type
from stockProject.stockApp.serializer import ProductSerializer, TypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductList(APIView):
    """
    API endpoint that allows products to be viewed or created.

    /products/

    """
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """
    API endpoint that allows types to be viewed or edited.
    """
class TypeList(APIView):

    def get(self, request):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








