from graphene_django.types import ObjectType

from .mutations import AddFoodCategory, AddFoodDetails, AddDeliveryPerson


# Quries

class Query(ObjectType):
    """
        query {
        allCategories {
            id
            categoryName
        }
        }

    """
    
    all_categories = List(FoodCategoryType)

    def resolve_all_categories(self, info, **kwargs):
        return FoodCategory.objects.all()


# Mutations

class Mutation(ObjectType):
    add_food_category = AddFoodCategory.Field()
    add_food_details = AddFoodDetails.Field()
    add_delivery_person = AddDeliveryPerson.Field()
