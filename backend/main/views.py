from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from . import models

class UserList(generics.ListCreateAPIView):
    queryset = models.USER.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = models.USER.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    
    
