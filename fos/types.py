from graphene_django.types import DjangoObjectType

from .models import FoodCategory, FoodDetails, CustomerDetails, DeliveryPerson, CustOrderStatus, CustOrderSelection


class FoodCategoryType(DjangoObjectType):
    class Meta:
        model = FoodCategory


class FoodDetailsType(DjangoObjectType):
    class Meta:
        model = FoodDetails


class CustomerDetailsType(DjangoObjectType):
    class Meta:
        model = CustomerDetails


class DeliveryPersonType(DjangoObjectType):
    class Meta:
        model = DeliveryPerson


class CustOrderStatusType(DjangoObjectType):
    class Meta:
        model = CustOrderStatus


class CustOrderSelectionType(DjangoObjectType):
    class Meta:
        model = CustOrderSelection
