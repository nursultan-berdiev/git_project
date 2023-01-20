from rest_framework import serializers
from .models import Item



class ItemSerializer(serializers.Serializer):


    class Meta:
        model = Item
        fields = "__all__"
