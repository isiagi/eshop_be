# urls
from django.urls import path

from .views import ProductListApiView, ProductDetailApiView

urlpatterns = [
    path('', ProductListApiView.as_view(), name='products'),
    path('<int:pk>', ProductDetailApiView.as_view(), name='product'),
]