from graphene import Int, String, InputObjectType, Mutation, ObjectType, Field, List

from .models import Employee
from .types import FoodCategoryType, FoodDetailsType, CustomerDetailsType, DeliveryPersonType, CustOrderStatus, CustOrderSelectionType


# Input Classes

class FoodCategoryInput(InputObjectType):
    category_name = String(required=True)


class FoodDetailsInput(InputObjectType):
    category_id = Int(required=True)
    food_name = String(required=True)
    price = Int(required=True)


class DeliveryPersonInput(InputObjectType):
    delivery_person_name = String(required=True)
    delivery_person_phone = Int(required=True)


# Mutations
 
class AddFoodCategory(Mutation):
    """
        mutation {
            addFoodCategory(data: {categoryName: "Test 03"}) {
                fields {
                    id
                    categoryName
                }
            }
        }    
    """
    fields = Field(FoodCategoryType)

    class Arguments:
        data = FoodCategoryInput(required=True)

    def mutate(self, info, data):
        food_category_data = Employee.add_food_category(self, **data)
        return AddFoodCategory(fields=food_category_data)


class AddFoodDetails(Mutation):
    """
        mutation {
            addFoodDetails(data: {categoryId: 20, foodName: "test 03", price: 50}) {
                fields {
                    id
                    foodName
                    price
                    categoryId {
                        categoryName
                    }
                }
            }
        }    
    """
    fields = Field(FoodDetailsType)

    class Arguments:
        data = FoodDetailsInput(required=True)

    def mutate(self, info, data):
        food_details_data = Employee.add_food_details(self, **data)
        return AddFoodDetails(fields=food_details_data)


class AddDeliveryPerson(Mutation):
    """
        mutation {
        addDeliveryPerson(data: {deliveryPersonName: "Test 01", deliveryPersonPhone: 111222}) {
            fields {
            id
            deliveryPersonName
            deliveryPersonPhone
            }
        }
        }
    """
    fields = Field(DeliveryPersonType)

    class Arguments:
        data = DeliveryPersonInput(required=True)

    def mutate(self, info, data):
        delivery_person_data = Employee.add_delivery_person(self, **data)
        return AddDeliveryPerson(fields=delivery_person_data)
