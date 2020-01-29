from datetime import datetime

from django.db import models 
from django.utils import timezone

from django.db.models import Sum, F


# Create your models here.
class FoodCategory(models.Model):
    """ Represents food categories """

    category_name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Food Category"


class FoodDetails(models.Model):
    """ Represents food details """

    category_id = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="category_id")
    food_name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Food Details"


class CustomerDetails(models.Model):
    """ Represents customer details """

    cust_name = models.CharField(max_length=64)
    cust_phone = models.IntegerField()
    cust_email = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Customer Details"


class DeliveryPerson(models.Model):
    """ Represents delivery person """

    delivery_person_name = models.CharField(max_length=64)
    delivery_person_phone = models.IntegerField()

    class Meta:
        verbose_name_plural = "Delivery Person"


class CustOrderStatus(models.Model):
    """ Represents order status """

    cust_id = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, related_name="cust_id")
    delivery_person_id = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, related_name="delivery_person_id", null=True, blank=True)     
    checkout_time = models.DateTimeField(default=timezone.now, blank=True) 
    estimated_time = models.DateTimeField(default=timezone.now, blank=True)
    order_status = models.CharField(max_length=64, null=True, blank=True)
    order_address = models.CharField(max_length=64, null=True, blank=True)
    bill_amount = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Customer Order Status"


class CustOrderSelection(models.Model):    
    """ Represents food ordered """

    order_id = models.ForeignKey(CustOrderStatus, on_delete=models.CASCADE, related_name="order_id")
    food_id = models.ForeignKey(FoodDetails, on_delete=models.CASCADE, related_name="food_id")  
    food_qty = models.IntegerField()

    class Meta:
        verbose_name_plural = "Customer Order Selection"


class Employee:
    """ Restaurant's end operation """

    def add_food_category(self, category_name):
        """ Insert a new food category """

        category_name = FoodCategory(category_name=category_name)
        category_name.save()
        return category_name

    def add_food_details(self, category_id, food_name, price):
        """ Insert new food details """

        food_details = FoodDetails(category_id_id=category_id, food_name=food_name, price=price)
        food_details.save()
        return food_details

    def add_delivery_person(self, delivery_person_name, delivery_person_phone):
        """ Insert new delivery person """

        details = DeliveryPerson(delivery_person_name=delivery_person_name, delivery_person_phone=delivery_person_phone)
        details.save()
        return details

    def assign_deliver_person_to_deliver_order(self, order_id, delivery_person_id):
        """ Update CustOrderStatus table to add deliver person to deliver order """

        assign_order = CustOrderStatus.objects.select_related('delivery_person_id').filter(id=order_id).update(delivery_person_id_id=delivery_person_id)
        return assign_order



class Customer:
    """ Customer's end operation """    

    def view_menu(self):
        """ Customer can view menu """

        menu = FoodDetails.objects.select_related('category_id').all()
        return menu

    def customer_signup(self, cust_name, cust_phone, cust_email):
        """ Add a new customer """

        signup = CustomerDetails(cust_name=cust_name, cust_phone=cust_phone, cust_email=cust_email)
        signup.save()
        return signup

    def customer_login(self, cust_id):
        """ Customer can login into their account """

        login = CustomerDetails.objects.get(pk=cust_id)
        return login

    def create_order_id(self, cust_id): 
        """ Generate order id """

        order_id = CustOrderStatus(cust_id_id=cust_id)
        order_id.save()
        return order_id

    def add_food_to_order(self, order_id, food_id, food_qty): 
        """ Add food items """

        add_food = CustOrderSelection(order_id_id=order_id, food_id_id=food_id, food_qty=food_qty)
        add_food.save()
        return add_food

    def remove_food_to_order(self, order_id, food_id):
        """ Remove food items """

        remove_food = CustOrderSelection.objects.filter(order_id_id=order_id).filter(food_id_id=food_id).delete()
        return remove_food

    def update_food_to_order(self, order_id, food_id, food_qty):
        """ Update food items """

        update_food = CustOrderSelection.objects.filter(order_id_id=order_id).filter(food_id_id=food_id).update(food_qty=food_qty)
        return update_food

    def checkout(self, order_id, order_status, order_address, checkout_time, estimated_time, bill_amount):
        """ Customer can checkout/confirm order """

        checkout_update = CustOrderStatus.objects.filter(id=order_id).update(order_status=order_status, order_address=order_address, checkout_time=checkout_time, estimated_time=estimated_time, bill_amount=bill_amount)
        return checkout_update

    def cancel_order(self, order_id, order_status):
        """ Cancel order """

        update_order = CustOrderStatus.objects.filter(id=order_id).update(order_status=order_status)
        return update_order



### Common functions used by both employees and customers

def get_grand_total(order_id):
    """ Employee/Customer can view the grand total of an order """

    grand_total = CustOrderSelection.objects.select_related('food_id').filter(order_id_id=order_id)
    price_per_food = []
    for i in grand_total:
        d = {
            "qty": i.food_qty,
            "price": i.food_id.price
            }
        price_per_food.append(d["qty"]*d["price"])
    bill_amount = sum(price_per_food)
    return bill_amount