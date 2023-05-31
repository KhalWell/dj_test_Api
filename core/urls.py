from django.urls import path, include
from .api import EmployeeApiSet, DepartmentApiSet
from rest_framework import routers

employee = routers.DefaultRouter()
department = routers.DefaultRouter()

employee.register(r'employee', EmployeeApiSet)
department.register(r'department', DepartmentApiSet)

urlpatterns = [
    path('', include(employee.urls)),
    path('', include(department.urls)),
]
