from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Product
        fields = '__all__'