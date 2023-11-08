from rest_framework import viewsets
from . import models
from . import serializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer