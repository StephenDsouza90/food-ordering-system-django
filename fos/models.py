from datetime import datetime

from django.db import models


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
    delivery_person_id = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, related_name="delivery_person_id")     
    checkout_time = models.DateTimeField(default=datetime.now, blank=True) # datetime.utcnow
    estimated_time = models.DateTimeField(default=datetime.now, blank=True) # datetime.utcnow
    order_status = models.CharField(max_length=64)
    order_address = models.CharField(max_length=64)
    bill_amount = models.IntegerField()
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


class Customer:
    """ Customer's end operation """    

    def view_menu(self):
        """ Customer can view menu """

        menu = FoodDetails.objects.select_related('category_id').all()
        return menu