from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserCreate

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('token/', obtain_auth_token, name='token'),
]