from django.db import models

class Type(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)

class Product(models.Model):
  name = models.CharField(max_length=200)
  cost_price = models.IntegerField(default=0)
  sale_price = models.IntegerField(default=0)
  product_type = models.ForeignKey(Type, on_delete=models.CASCADE)
