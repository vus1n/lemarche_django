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



@api_view(['GET','POST'])
def create_list_myads(request,id):
    user  = UserModel.objects.get(name=id)
    if request.method == 'GET':
        products = Product.objects.filter(userId = user.userId)
        data = ProductSerializer(products,many=True)
        return Response({"data":data.data})
    elif request.method == 'POST':
        category = request.data['category']
        category_model = Category.objects.get(categoryName = category)
        title = request.data['title']
        brand = request.data['brand']
        imgUrl = request.data['img']
        price = request.data['price']
        ad = Product.objects.create(userId=user,categoryId=category_model,title=title,brand=brand,imgUrl=imgUrl,price=price)
        ad.save()
        ad_data = ProductSerializer(ad)
        return Response(ad_data.data)



@api_view(['GET','PUT'])
def retrieve_update_acc(request,id):
    if request.method == 'GET':
        user = UserModel.objects.get(name=id)
        user_serializer = UserModelSerializer(user)
        return Response({"data":user_serializer.data})
    elif request.method == 'PUT':
        name = request.data['name']
        email = request.data['email']
        pic = request.data['pic']
        contactNo = request.data['contact']
        location = request.data['location']
        user_model = UserModel.objects.update(name=name,email=email,pic=pic,contactNo=contactNo,location=location)
       
        user_serializer = UserModelSerializer(user_model)
        return Response(user_serializer.data)
