from stockProject.stockApp.models import Product, Type
from stockProject.stockApp.serializer import ProductSerializer, TypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.pagination import PageNumberPagination
import code

"""
debugging lines

import code
code.interact(local=dict(globals(), **locals()))

"""
class ProductList(APIView):
    """
    API endpoint that allows products to be viewed or created.

    /products/

    """
    def get(self, request):
        products = Product.objects.all()
        paginator = PageNumberPagination()
        if request.GET.get('page_size') != None:
            paginator.page_size = request.GET.get('page_size')
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        product.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class TypeList(APIView):

    def get(self, request):
        types = Type.objects.all()
        paginator = PageNumberPagination()
        if request.GET.get('page_size') != None:
            paginator.page_size = request.GET.get('page_size')
        page = paginator.paginate_queryset(types, request)
        serializer = TypeSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeDetail(APIView):

    def get(self, request, pk):
        typeobject = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(typeobject)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        typeobject = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(typeobject)
        typeobject.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        typeobject = get_object_or_404(Type,pk=pk)
        serializer = TypeSerializer(typeobject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

