import json

from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Employee, Customer, DeliveryPerson, get_grand_total, view_order, view_order_status, view_order_total


def index(request):
    """ Home page """

    return HttpResponse("Hello, Welcome to the Food Ordering System App!")


def request_method(request):
    """ Func that handles methods and decoding data """

    methods = ['POST', 'PUT', 'DELETE', 'GET']
    if request.method in methods:
        json_data = json.loads(request.body)
        return json_data


### Employee's func and routes

@csrf_exempt
def add_food_category(request):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"category_name\":\"test\"}" http://127.0.0.1:8000/employees/add-food-category
    """

    json_data = request_method(request)
    category_name = json_data['category_name']
    food_category = Employee.add_food_category(request, category_name)
    DictObj = {
        "category_id": food_category.id,
        "category_name": food_category.category_name
        }
    return JsonResponse(DictObj)


@csrf_exempt
def add_food_details(request):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"category_id_id\":1, \"food_name\":\"test\", \"price\":5}" http://127.0.0.1:8000/employees/add-food-details
    """

    json_data = request_method(request)
    category_id = json_data['category_id_id']
    food_name = json_data['food_name']
    price = json_data['price']
    food_details = Employee.add_food_details(request, 
        category_id, food_name, price)
    DictObj = {
        "category_id": food_details.category_id_id,
        "food_id": food_details.id,
        "food_name": food_details.food_name,
        "food_price": food_details.price
        }
    return JsonResponse(DictObj)


@csrf_exempt
def add_delivery_person(request):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"delivery_person_name\":\"test\", \"delivery_person_phone\":111}" http://127.0.0.1:8000/employees/add-delivery-person
    """

    json_data = request_method(request)
    delivery_person_name = json_data['delivery_person_name']
    delivery_person_phone = json_data['delivery_person_phone']
    del_person_details = Employee.add_delivery_person(request, 
        delivery_person_name, delivery_person_phone)
    DictObj = {
        "delivery_person_id": del_person_details.id,
        "delivery_person_name": del_person_details.delivery_person_name,
        "delivery_person_phone": del_person_details.delivery_person_phone
        }
    return JsonResponse(DictObj)


@csrf_exempt
def assign_deliver_person_to_deliver_order(request):
    """
    >> curl -H "Content-Type: application/json" -X PUT -d "{\"order_id\":1, \"delivery_person_id\":1}" http://127.0.0.1:8000/employees/assign-deliver-person-to-deliver-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    delivery_person_id = json_data["delivery_person_id"]
    Employee.assign_deliver_person_to_deliver_order(request, 
        order_id, delivery_person_id)
    DictObj = {
        "order_id": order_id,
        "delivery_person_id": delivery_person_id
        }
    return JsonResponse(DictObj)


@csrf_exempt
def update_order(request):
    """
    >> curl -H "Content-Type: application/json" -X PUT -d "{\"order_id\":1, \"order_status\":\"En route\"}" http://127.0.0.1:8000/employees/update-order
    >> curl -H "Content-Type: application/json" -X PUT -d "{\"order_id\":1, \"order_status\":\"Delivered\"}" http://127.0.0.1:8000/employees/update-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    order_status = json_data["order_status"]
    DeliveryPerson.update_order(request, order_id, order_status)
    DictObj = {
        "order_id": order_id,
        "order_status": order_status
        }
    return JsonResponse(DictObj)


@csrf_exempt
def view_sales_today(request):
    """
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_status\":\"'Delivered'\"}" http://127.0.0.1:8000/employees/view-sales-today
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_status\":\"'En route'\"}" http://127.0.0.1:8000/employees/view-sales-today
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_status\":\"'Checked out'\"}" http://127.0.0.1:8000/employees/view-sales-today
    """

    json_data = request_method(request)
    order_status = json_data["order_status"]
    sales_today = Employee.view_sales_today(request, order_status)
    result = []
    for i in sales_today:
        DictObj = {
            "order_id": i[0],
            "customer_name": i[1],
            "order_status": i[2],
            "bill_amount": i[3],
            "date_time": i[4]
            }
        result.append(DictObj)
    return JsonResponse(result, safe=False)


@csrf_exempt
def sum_revenue_today(request):
    """
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_status\":\"'Delivered'\"}" http://127.0.0.1:8000/employees/sum-revenue-today
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_status\":\"'En route'\"}" http://127.0.0.1:8000/employees/sum-revenue-today
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_status\":\"'Checked out'\"}" http://127.0.0.1:8000/employees/sum-revenue-today
    """

    json_data = request_method(request)
    order_status = json_data["order_status"]
    sum_rev_today = Employee.sum_revenue_today(request, order_status)
    for i in sum_rev_today:
        DictObj = {
            "today_revenue": i[0]
            }
    return JsonResponse(DictObj, safe=False)


@csrf_exempt
def delete_order(request):
    """
    >> curl -H "Content-Type: application/json" -XDELETE -d "{\"order_id\":1}" http://127.0.0.1:8000/employees/delete-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    Employee.delete_order(request, order_id)
    DictObj = {
        "order_id": order_id
        }
    return JsonResponse(DictObj)


### Customer's func and routes

@csrf_exempt
def view_menu(request):
    """
    >> curl http://127.0.0.1:8000/customers/view-menu
    """

    result = []
    menu = Customer.view_menu(request)
    for m in menu:
        DictObj = {
            "category_id": m.category_id.id,
            "category_name": m.category_id.category_name,
            "food_id": m.id,
            "food_name": m.food_name,
            "price": m.price
            }
        result.append(DictObj)
    return JsonResponse(result, safe=False)


@csrf_exempt
def customer_signup(request):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"cust_name\":\"test\", \"cust_phone\":111, \"cust_email\":\"test\"}" http://127.0.0.1:8000/customers/signup
    """

    json_data = request_method(request)
    cust_name = json_data['cust_name']
    cust_phone = json_data['cust_phone']
    cust_email = json_data['cust_email']
    cust_details = Customer.customer_signup(request, cust_name, 
        cust_phone, cust_email)
    DictObj = {
        "cust_id": cust_details.id,
        "cust_name": cust_details.cust_name,
        "cust_phone": cust_details.cust_phone,
        "cust_email": cust_details.cust_email
        }
    return JsonResponse(DictObj)


@csrf_exempt
def customer_login(request, cust_id):
    """
    >> curl http://127.0.0.1:8000/customers/1/login
    """

    cust = Customer.customer_login(request, cust_id)
    DictObj = {
        "cust_id": cust.id,
        "cust_name": cust.cust_name
    }
    return JsonResponse(DictObj, safe=False)


@csrf_exempt
def create_order_id(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"cust_id\":1}" http://127.0.0.1:8000/customers/1/create-order
    """

    json_data = request_method(request)
    cust_id = json_data['cust_id']
    gen_order_id = Customer.create_order_id(request, cust_id)
    DictObj = {
        "order_id": gen_order_id.id,
        "cust_id": gen_order_id.cust_id_id
        }
    return JsonResponse(DictObj)


@csrf_exempt
def add_food_to_order(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X POST -d "{\"order_id\":1, \"food_id\":1, \"food_qty\":1}" http://127.0.0.1:8000/customers/1/add-food-to-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    food_id = json_data["food_id"]
    food_qty = json_data["food_qty"]
    add_food = Customer.add_food_to_order(request, order_id, 
        food_id, food_qty)
    DictObj = {
        "order_id": add_food.order_id_id,
        "food_id": add_food.food_id_id,
        "food_qty": add_food.food_qty
        }
    return JsonResponse(DictObj)


@csrf_exempt
def remove_food_to_order(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -XDELETE -d "{\"order_id\":1, \"food_id\":2}" http://127.0.0.1:8000/customers/1/remove-food-to-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    food_id = json_data["food_id"]
    Customer.remove_food_to_order(request, order_id, food_id)
    DictObj = {
        "order_id": order_id,
        "food_id": food_id
        }
    return JsonResponse(DictObj)


@csrf_exempt
def update_food_to_order(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X PUT -d "{\"order_id\":1, \"food_id\":1, \"food_qty\":1}" http://127.0.0.1:8000/customers/1/update-food-to-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    food_id = json_data["food_id"]
    food_qty = json_data["food_qty"]
    Customer.update_food_to_order(request, order_id, food_id, food_qty)
    DictObj = {
        "order_id": order_id,
        "food_id": food_id,
        "food_qty": food_qty
        }
    return JsonResponse(DictObj)


@csrf_exempt
def checkout(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X PUT -d "{\"order_id\":1, \"order_address\":\"Karachi\"}" http://127.0.0.1:8000/customers/1/checkout
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    order_status = "Checked out"
    order_address = json_data["order_address"]
    checkout_time = timezone.now()
    estimated_time = checkout_time + timedelta(minutes=30)
    bill_amount = get_grand_total(order_id)
    Customer.checkout(request, order_id, order_status, 
        order_address, checkout_time, estimated_time, bill_amount)
    DictObj = {
        "order_id": order_id,
        "order_status": order_status,
        "order_address": order_address,
        "estimated_time": estimated_time,
        "bill_amount": bill_amount
        }
    return JsonResponse(DictObj)


@csrf_exempt
def cancel_order(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X PUT -d "{\"order_id\":1}" http://127.0.0.1:8000/customers/1/cancel-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    order_status = "Cancelled"
    Customer.cancel_order(request, order_id, order_status)
    DictObj = {
        "order_id": order_id,
        "order_status": order_status
        }
    return JsonResponse(DictObj)


### Common func and routes

@csrf_exempt
def view_order_by_id(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_id\":1}" http://127.0.0.1:8000/customers/1/view-order
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_id\":1}" http://127.0.0.1:8000/employees/1/view-order
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    view_order_item = view_order(order_id)
    result = []
    for i in view_order_item:
        DictObj = {
            "food_category": i.food_id.category_id.category_name,
            "food_name": i.food_id.food_name,
            "food_price": i.food_id.price,
            "food_quantity": i.food_qty,
            "total_per_item": (i.food_id.price*i.food_qty)
            }
        result.append(DictObj)
    return JsonResponse(result, safe=False)


@csrf_exempt
def view_order_status_by_id(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_id\":1}" http://127.0.0.1:8000/customers/1/view-order-status
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_id\":1}" http://127.0.0.1:8000/employees/1/view-order-status
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    view_status = view_order_status(order_id)
    for i in view_status:
        DictObj = {
            "customer_name": i.cust_id.cust_name,
            "order_id": i.id,
            "order_status": i.order_status,
            "total_bill": i.bill_amount,
            "delivery_person_name": i.delivery_person_id.delivery_person_name
            }
    return JsonResponse(DictObj)


@csrf_exempt
def view_order_total_by_id(request, cust_id):
    """
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_id\":1}" http://127.0.0.1:8000/customers/1/view-order-total
    >> curl -H "Content-Type: application/json" -X GET -d "{\"order_id\":1}" http://127.0.0.1:8000/employees/1/view-order-total
    """

    json_data = request_method(request)
    order_id = json_data["order_id"]
    view_order = view_order_total(order_id)
    for i in view_order:
        DictObj = {
            "customer_name": i.cust_id.cust_name,
            "order_id": i.id,
            "grand_total": i.bill_amount
            }
    return JsonResponse(DictObj)