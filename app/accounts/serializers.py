from rest_framework import serializers

from .models import User


class UserRegister(serializers.ModelSerializer):
    password_2 = serializers.CharField(max_length=64, write_only=True)
    password = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_2']

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_2 = validated_data.pop('password_2')
        if password != password_2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
