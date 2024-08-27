from django.urls import path

from .views import CategoryListApiView, CategoryDetailApiView

urlpatterns = [
    path('', CategoryListApiView.as_view(), name='categories'),
    path('<int:pk>', CategoryDetailApiView.as_view(), name='category'),
]