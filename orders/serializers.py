from rest_framework import serializers
from . import models

class OrderSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.OrderModel
        fields = "__all__"

