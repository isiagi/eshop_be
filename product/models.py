from django.db import models
from category.models import Category
from userauth.models import CustomUser

# Create your models here.
# product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.OneToOneField(Category, to_field='name', unique=True, on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name