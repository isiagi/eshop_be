from django.db import models
from category.models import Category
from userauth.models import CustomUser

# Create your models here.
# product model

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to=upload_to, null=True, blank=True)
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    def __str__(self):
        return self.name