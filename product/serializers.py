from rest_framework import serializers
from .models import Product
from category.models import Category
from userauth.models import CustomUser

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'