from django.urls import path
from . import views

urlpatterns = [
    path("", views.employeeList, name='employee-list'),
    path("add_emp/", views.addEmployee, name='add-employee'),
    path("update_employee/<employee_id>", views.updateEmployee, name='update-employee'),
    path("delete_employee/<employee_id>", views.deleteEmployee, name='delete-employee'),
]