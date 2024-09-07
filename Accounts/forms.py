from django import forms
from django.contrib.auth.models import User


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ["__all__"]


class profileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
