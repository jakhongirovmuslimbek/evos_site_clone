from rest_framework import viewsets
from .serializers import *
from .models import *

class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
