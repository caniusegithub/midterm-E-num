from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)