from django.contrib import admin

from .models import FoodCategory, FoodDetails, CustomerDetails, CustOrderSelection, CustOrderStatus, DeliveryPerson

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(FoodDetails)
admin.site.register(CustomerDetails)
admin.site.register(CustOrderSelection)
admin.site.register(CustOrderStatus)
admin.site.register(DeliveryPerson)