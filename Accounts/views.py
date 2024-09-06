from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import loginForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data["username"],
            )
            user.set_password(data["password1"])
            user.save()
            return redirect("home")
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "register.html", context)


def user_login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("home")
    form = loginForm()
    context = {"form": form}
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")
