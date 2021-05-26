# Appointments-Django

## Python Version 3.9.5

### REST API using Django Rest Framework. 
This project will be used as the boilerplate for a custom appointments web app for a nail salon in Denver, Colorado.

Basic authentication is used (Django encrypts the passwords) with authentication tokens available to the website front-end. There are 3 types of users:
1. admin
    - has permissions for everything
2. manager
    - can add new Users (managers) with is_staff=True access
    - can add new Employees, Customers, and Appointments 
    - otherwise same access as api_user but can see more detail for employees and customers
3. api_user
    - can add Customers and Appointments

### Django Website Front-End
Django website that connects to the appointments API and lets users view and make appointments.