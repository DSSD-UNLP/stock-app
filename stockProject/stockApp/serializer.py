from stockProject.stockApp.models import Type, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'cost_price', 'sale_price', 'product_type')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'description')