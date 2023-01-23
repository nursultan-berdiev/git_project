from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    count = serializers.IntegerField()

    def create(self, validated_data):
        item = Item.objects.create(**validated_data)
        return item


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['count']
