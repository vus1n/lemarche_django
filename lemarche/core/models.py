from django.db import models
from django.contrib.auth.models import User
import uuid

class UserModel(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email= models.CharField(max_length = 50)
    name =models.CharField(max_length = 50)
    pic = models.TextField(max_length=200, null =True, blank =True)
    contactNo = models.IntegerField()
    location = models.TextField(max_length=200, null =True, blank =True)
    def __str__(self):
        return self.name

class Category(models.Model):
    categoryId =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryName = models.CharField(max_length = 50)
    imgUrl =models.TextField(max_length=200, null =True, blank =True)

    def __str__(self):
        return self.categoryName
    

class Product(models.Model):
    productId =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.ForeignKey(UserModel,on_delete = models.CASCADE)
    
    categoryId = models.ForeignKey(Category,on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 50, null =True, blank =True)
    description = models.TextField(max_length=600, null =True, blank =True)
    price = models.IntegerField()
    datePosted = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)
    imgUrl = models.TextField(max_length=200, null =True, blank =True)
    liked_by = models.ManyToManyField(UserModel,related_name="liked_by", blank=True)
    


    def __str__(self):
        return self.title
    


