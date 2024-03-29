from rest_framework import serializers

from .models import Check


class ItemsSerializer(serializers.Serializer):
    """Серіалізатор для даних замовлення."""
    name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(min_value=1)
    unit_price = serializers.IntegerField(min_value=1)


class ClientSerializer(serializers.Serializer):
    """Серіалізатор даних клієнта."""
    name = serializers.CharField(max_length=255)
    phone = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    """Серіалізатор для прийому замовлень."""
    id = serializers.IntegerField(min_value=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    items = ItemsSerializer(many=True)
    client = ClientSerializer()
    address = serializers.CharField(max_length=255)
    point_id = serializers.IntegerField(min_value=1)


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ('id',)
