from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class OrderItem(models.Model):
    order_id=models.CharField(max_length=20,null=True,blank=True)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=30)
    category_id=models.IntegerField()
    category_name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=20,decimal_places=2)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    allocation=models.BooleanField(default=False)
    table_num=models.IntegerField()
    prepared_by=models.TextField(blank=True,null=True)


    class Meta:
        verbose_name='OrderItem'
        verbose_name_plural='OrderItems'

    def __str__(self):
        return '{}' .format(self.product_name)


class Chef(models.Model):
    chef_name=models.CharField(max_length=30)
    description=models.TextField(null=True,blank=True)
    mobile=models.CharField(max_length=10)
    status=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Chef'
        verbose_name_plural='Chefs'

    def __str__(self):
        return '{}' .format(self.chef_name)

class Category(models.Model):
    category_id=models.IntegerField()
    category_name=models.CharField(max_length=20)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    
    def __str__(self):
        return '{}' .format(self.category_name)















    
