import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Employee, Customer


# Create your views here.
def index(request):
    """ Home page """
    #TODO: Allow a customer to view menu and register/login
    #TODO: find a way to use csrf in python code     
    return HttpResponse("Hello, Welcome to the Food Ordering System App!")

@csrf_exempt
def add_food_category(request):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"category_name\":\"test\"}" http://127.0.0.1:8000/employees/add-food-category
    """

    if request.method == 'POST':
        json_data = json.loads(request.body)
        category_name = json_data['category_name']
        food_category = Employee.add_food_category(request, category_name)
        catDictObj = {
            "category_id": food_category.id,
            "category_name": food_category.category_name
            }
        return JsonResponse(catDictObj)


@csrf_exempt
def add_food_details(request):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"category_id_id\":3, \"food_name\":\"Suflay\", \"price\":5}" http://127.0.0.1:8000/employees/add-food-details
    """

    if request.method == 'POST':
        json_data = json.loads(request.body)
        category_id = json_data['category_id_id']
        food_name = json_data['food_name']
        price = json_data['price']
        food_details = Employee.add_food_details(request, category_id, food_name, price)
        detDictObj = {
            "category_id": food_details.category_id_id,
            "food_id": food_details.id,
            "food_name": food_details.food_name,
            "food_price": food_details.price
        }
        return JsonResponse(detDictObj)


@csrf_exempt
def add_delivery_person(request):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"delivery_person_name\":\"new_test\", \"delivery_person_phone\":111}" http://127.0.0.1:8000/employees/add-delivery-person
    """

    if request.method == 'POST':
        json_data = json.loads(request.body)
        delivery_person_name = json_data['delivery_person_name']
        delivery_person_phone = json_data['delivery_person_phone']
        details = Employee.add_delivery_person(request, delivery_person_name, delivery_person_phone)
        detDictObj = {
            "delivery_person_id": details.id,
            "delivery_person_name": details.delivery_person_name,
            "delivery_person_phone": details.delivery_person_phone
        }
        return JsonResponse(detDictObj)


@csrf_exempt
def view_menu(request):
    """
    >> curl http://127.0.0.1:8000/customers/view-menu
    """

    if request.method == 'GET':
        menu = Customer.view_menu(request)
        result = []
        for m in menu:
            foodDictObj = {
                "category_id": m.category_id.id,
                "category_name": m.category_id.category_name,
                "food_id": m.id,
                "food_name": m.food_name,
                "price": m.price
                }
            result.append(foodDictObj)
        return JsonResponse(result, safe=False)