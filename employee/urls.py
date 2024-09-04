from django.urls import path
from . import views
from employer.views import employer

urlpatterns = [
    path("", views.index, name="home"),
    path("employee/", views.employee, name="employee"),
    path("employer/", employer, name="employer"),
    path("employee/create/", views.createEmployee, name="create-employee"),
    path("employee/delete/<str:pk>", views.deleteEmployee, name="delete-employee"),
    path("employee/update/<str:pk>", views.updateEmployee, name="update-employee"),
]
