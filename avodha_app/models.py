from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=150)
    des = models.TextField()
    img = models.ImageField(upload_to='images')
    price = models.IntegerField()


