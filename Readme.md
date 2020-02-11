# Food Ordering System (written with Django)

## Introduction

This application is a simple food ordering system written in Django which has two interfaces i.e. Employee and Customer.

Both users can interact with the system through several options to perfrom an activity.

The Employee and Customer interface are modeled through classes and the options are mapped to the methods in these classes.

The options available to the Employee are add food category, add food details, add delivery person, assign delivery person to an order, update food order, view food details, view revenue and delete order.

The options available to the Customer are view menu, sign up and log in, create an order, checkout and view order details and status.

## Tables

There are several classes that inherit Models from Django in order to create tables. 

These classes are Food Category, Food Details, Customer Details, Customer Order Selection, Customer Order Status and Delivery Person.

The table names and columns are created in the database by Django when the app initially starts and a connection is also made to the database by Django's internal functions. 

### Purpose of the tables

The purpose of the tables in the databse is to store records when the Employee or Customer performs a certain activity.

For example - If an employee adds a food category and food detail so this will be stored in the Food Caterogy table and Food Details table respectively. When the customer will view the menu, so they will be able to see these items.


## How to run locally:


```
>> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 11, 2020 - 12:48:34
Django version 3.0.2, using settings 'foodorderingsystem.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Request for viewing menu
```
[11/Feb/2020 12:49:38] "GET /customers/view-menu HTTP/1.1" 200 470
```
![View menu](https://github.com/StephenDsouza90/food-ordering-system-django/blob/fos_django/Screenshots/view_menu.jpg)