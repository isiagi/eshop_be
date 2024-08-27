from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductListApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
