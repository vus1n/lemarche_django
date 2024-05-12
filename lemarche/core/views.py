from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category,Product,UserModel
from .serializers import CategorySerializer,ProductSerializer,UserModelSerializer

@api_view(['GET'])
def list_products(request,id):
    if id != 'All':
        category = Category.objects.get(categoryName=id)
        products = Product.objects.filter(categoryId=category.categoryId)
        
    else:
        products = Product.objects.all()
    
    user = [product.userId for product in products]

    products_serializer = ProductSerializer(products,many=True)
    userSerializer  =UserModelSerializer(user,many=True)
    combined_data =[]
    for product in products_serializer.data:
        user_data =next((item for item in userSerializer.data ), None)
        combined_data.append({**product , "user":user_data})
    return Response({"data":combined_data})

@api_view(['GET'])
def list_categories(request):
    categorys = Category.objects.all()
    categorys_serializer = CategorySerializer(categorys,many=True)
    return Response({"data":categorys_serializer.data})

@api_view(['GET'])
def list_liked_products(request,id):
    user = UserModel.objects.get(name=id)
    liked_products = Product.objects.filter(liked_by=user)
    data = ProductSerializer(liked_products,many=True)
    return Response({"data":data.data})


#make it create_list_myads
@api_view(['GET'])
def create_list_myads(request,id):
    user  = UserModel.objects.get(name=id)
    products = Product.objects.filter(userId = user.userId)
    data = ProductSerializer(products,many=True)
    return Response({"data":data.data})

#make it retreive_update_acc
@api_view(['GET'])
def retrieve_update_acc(request,id):
    user = UserModel.objects.get(name=id)
    user_serializer = UserModelSerializer(user,many=True)
    return Response({"data":user_serializer.data})

