from distutils.command.upload import upload
from pkgutil import extend_path
from statistics import mode
from email.mime import image
from multiprocessing.dummy import active_children
from unicodedata import category, name
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to = 'photos/%y/%m/%d')
    is_active = models.BooleanField(default=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name


    class Meta: 
            ordering = ('-id',)

            
class Order(models.Model):
    productid = models.IntegerField()
    user_id = models.IntegerField()
    num =models.IntegerField()