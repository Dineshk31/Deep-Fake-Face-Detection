from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.USER
        fields = ['id', 'full_name', 'email', 'password', 'mobile']