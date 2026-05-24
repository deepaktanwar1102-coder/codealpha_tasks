from django.urls import path
from .views import product_list, register_user, create_order

urlpatterns = [
    path('products/', product_list),
    path('register/', register_user),
    path('order/', create_order),
]