from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]