from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Person


# Create your views here.
def index(request):
    return render(request, "base.html")


def employee(request):
    if request.method == "POST":
        pass
        # data = request.POST
        # email = data["email"]
        # password = data["password"]
        # context = {"email": email, "password": password}
    else:
        employees = Person.objects.all()
        form = EmployeeForm()
        context = {"form": form, "employees": employees}

    return render(request, "employee/employee.html", context)


def createEmployee(request):
    if request.method == "POST":
        data = request.POST
        firstName = data.get("firstName")
        lastName = data.get("lastName")
        email = data.get("email")
        Person.objects.create(first_name=firstName, last_name=lastName, email=email)
        return redirect("employee")

    return render(request, "employee/create-employee.html")


def updateEmployee(request, pk):
    if request.method == "POST":
        data = request.POST
        newFirstName = data.get("newFirstName")
        newLastName = data.get("newLastName")
        newEmail = data.get("newEmail")
        obj = Person.objects.get(id=pk)
        obj.first_name = newFirstName
        obj.last_name = newLastName
        obj.email = newEmail
        obj.save()
        return redirect("employee")
    return render(request, "employee/update-employee.html")


def deleteEmployee(request, pk):
    if request.method == "GET":
        obj = Person.objects.get(id=pk)
        obj.delete()
        return redirect("employee")
