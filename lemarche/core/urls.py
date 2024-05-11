from django.urls import path
from . import views

urlpatterns = [
    path('products/<str:id>/',views.products),
    path('category/',views.categories),
    path('liked_products/<str:id>/',views.liked_products),
    path('my_ads/<str:id>/',views.my_ads),
    path('user/<str:id>/',views.my_acc),
]

