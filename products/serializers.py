from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = "__all__"

    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request", None)
        if request.method == "GET":
            self.fields['category'] = CategorySerializer()

