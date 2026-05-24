from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Customer, Order
import json


def product_list(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

        customer = Customer.objects.create(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )

        return JsonResponse({
            "message": "User Registered Successfully"
        })
        
@csrf_exempt
def create_order(request):

    if request.method == "POST":

        data = json.loads(request.body)

        order = Order.objects.create(
            customer=data['customer'],
            product=data['product'],
            quantity=data['quantity']
        )

        return JsonResponse({
            "message": "Order Stored Successfully"
        })