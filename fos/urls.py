from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("employees/add-food-category", views.add_food_category, name="food_category"),
    path("employees/add-food-details", views.add_food_details, name="food_details"),
    path("employees/add-delivery-person", views.add_delivery_person, name="delivery_person"),
    path("employees/assign-deliver-person-to-deliver-order", views.assign_deliver_person_to_deliver_order, name="assign_order"),
    path("customers/view-menu", views.view_menu, name="menu"),
    path("customers/signup", views.customer_signup, name="signup"),
    path("customers/<int:cust_id>/login", views.customer_login, name="login"),
    path("customers/<int:cust_id>/create-order", views.create_order_id, name="order_id"),
    path("customers/<int:cust_id>/add-food-to-order", views.add_food_to_order, name="add_food"),
    path("customers/<int:cust_id>/remove-food-to-order", views.remove_food_to_order, name="remove_food"),
    path("customers/<int:cust_id>/update-food-to-order", views.update_food_to_order, name="update_food"),
    path("customers/<int:cust_id>/checkout", views.checkout, name="checkout"),
    path("customers/<int:cust_id>/cancel-order", views.cancel_order, name="cancel_order"),
]