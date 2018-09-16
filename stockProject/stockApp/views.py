from stockProject.stockApp.models import Product, Type
from rest_framework import viewsets
from stockProject.stockApp.serializer import ProductSerializer, TypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows types to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer