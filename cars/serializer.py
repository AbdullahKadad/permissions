from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car 
        fields = ('owner', 'model', 'brand', 'price')
