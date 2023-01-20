from django.shortcuts import render

from .models import User
from .serializers import UserRegister

from rest_framework import generics


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegister
