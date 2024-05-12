from django.urls import path
from . import views

urlpatterns = [
    path('products/<str:id>/',views.list_products),
    path('categories/',views.list_categories),
    path('user/<str:id>/liked_products/',views.list_liked_products),
    path('user/<str:id>/my_ads/',views.create_list_myads),
    path('user/<str:id>/',views.retrieve_update_acc),
]
