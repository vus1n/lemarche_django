from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    products_serializer = ProductSerializer(products,many=True)
    return Response(products_serializer.data)

@api_view(['GET'])
def categories(request):
    categorys = Category.objects.all()
    categorys_serializer = CategorySerializer(categorys,many=True)
    return Response(categorys_serializer.data)