from rest_framework import serializers

from .models import Check, Printer


class CreateChecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = ('id', 'point_id', 'name', 'point_id')


class ChecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ('id', 'printer_id', 'defined_type', 'order', 'status')
