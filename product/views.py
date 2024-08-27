from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class ProductListApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


    def perform_create(self, serializer):
        if not self.request.user.user_type == 'seller':
            raise PermissionDenied("Only seller can add product")
        
        serializer.save(seller=self.request.user)


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
