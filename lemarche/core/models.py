from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    categoryId = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length = 50)

    def __str__(self):
        return self.categoryName
    

class Product(models.Model):
    productId = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(User,on_delete = models.CASCADE)
    categoryId = models.ForeignKey(Category,on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length=200, null =True, blank =True)
    price = models.IntegerField()
    datePosted = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)
    imgUrl = models.TextField(max_length=200, null =True, blank =True)

    def __str__(self):
        return self.title



