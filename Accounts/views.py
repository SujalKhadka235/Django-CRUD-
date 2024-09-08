from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import loginForm, profileForm, profileModelForm
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


def user_profile(request):
    if request.method == "POST":
        profile_form = profileModelForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if profile_form.is_valid():
            profile_form.save()

        data = request.POST
        firstName = data["first_name"]
        lastName = data["last_name"]
        user_obj = User.objects.get(id=request.user.id)
        user_obj.first_name = firstName
        user_obj.last_name = lastName
        user_obj.save()
        return redirect("home")
    form = profileForm(
        initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "images": request.user.profile.image.url,
        }
    )
    context = {"form": form, "profileForm": profileModelForm()}
    return render(request, "profile.html", context)
