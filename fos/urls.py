from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("employees/add-food-category", views.add_food_category, name="food_category"),
    path("employees/add-food-details", views.add_food_details, name="food_details"),
    path("employees/add-delivery-person", views.add_delivery_person, name="delivery_person"),
    path("customers/view-menu", views.view_menu, name="menu"),
]