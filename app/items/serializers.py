from rest_framework import serializers
from .models import Item


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['count']

