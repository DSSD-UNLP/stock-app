from stockProject.stockApp.models import Product, Type
from stockProject.stockApp.serializer import ProductSerializer, TypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
import code
from stockProject.stockApp.filter import ProductFilter,TypeFilter
from stockProject.stockApp.paginator_wrapper import StandardResultsSetPagination

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
        products = ProductFilter(Product.objects.all(), request).products()
        paginator       = StandardResultsSetPagination()    
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
    def patch(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        if product.stock > 0:
            product.stock = product.stock - 1
            product.save()
            status_code    = status.HTTP_200_OK
            status_message = "ok"
            message        = "Se decremento el stock"
        else:
            status_code    = status.HTTP_400_BAD_REQUEST
            status_message = "error"
            message        = "No hay stock del producto"

        response_message   = {
            "status": status_message, 
            "message":message
        }

        return Response(response_message, status = status_code)
class TypeList(APIView):

    def get(self, request):
        types = TypeFilter(Type.objects.all(),request).types()
        paginator = StandardResultsSetPagination()
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

