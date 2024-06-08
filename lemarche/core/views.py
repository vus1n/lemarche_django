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
    user = UserModel.objects.get(email=id)
    liked_products = Product.objects.filter(liked_by=user)
    data = ProductSerializer(liked_products,many=True)
    return Response({"data":data.data})



@api_view(['GET','POST'])
def create_list_myads(request,id):
    user  = UserModel.objects.get(email=id)
    if request.method == 'GET':
        products = Product.objects.filter(userId = user)
        data = ProductSerializer(products,many=True)
        return Response({"data":data.data})
    elif request.method == 'POST':
        
        category = request.data['category']
        category_model = Category.objects.get(categoryName = category)
        title = request.data['title']
        brand = request.data['brand']
        description = request.data['description']
        imgUrl = request.data['imgUrl']
        price = request.data['price']
        ad = Product.objects.create(userId=user,categoryId=category_model,title=title,brand=brand,description=description,imgUrl=imgUrl,price=price)
        ad.save()
        ad_data = ProductSerializer(ad)
        return Response(ad_data.data)



@api_view(['GET', 'PUT'])
def retrieve_update_acc(request, id):
    if request.method == 'GET':
        try:
            user = UserModel.objects.get(email=id)
            user_serializer = UserModelSerializer(user)
            return Response({"data": user_serializer.data})
        except UserModel.DoesNotExist:
            user = UserModel.objects.create(email=id, name='new user', contactNo=000000)
            user.save()
            user_serializer = UserModelSerializer(user)
            return Response({"data": user_serializer.data})

    elif request.method == 'PUT':
        try:
            user = UserModel.objects.get(email=id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found."})

        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'pic': request.data.get('pic'),
            'contactNo': request.data.get('contact'),
            'location': request.data.get('location')
        }
        user_serializer = UserModelSerializer(user, data=data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
