from testapp.models import OrderItem
from rest_framework import serializers

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'

