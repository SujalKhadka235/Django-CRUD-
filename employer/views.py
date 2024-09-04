from django.shortcuts import render, redirect
from .forms import EmployerForm


# Create your views here.
def employer(request):
    if request.method == "POST":
        form = EmployerForm(request.POST)
        print(form.cleaned_data)
    form = EmployerForm()
    context = {"form": form}
    return render(request, "employer/employer.html", context)
