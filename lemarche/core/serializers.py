from rest_framework.serializers import ModelSerializer
from .models import Product,Category,UserModel,Campus

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields ='__all__'

class CampusSerializer(ModelSerializer):
    class Meta:
        model = Campus
        fields ='__all__'