from rest_framework import serializers
from .models import *


class CotegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotegory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'cotegory', 'price', ]


class ProductPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = '__all__'