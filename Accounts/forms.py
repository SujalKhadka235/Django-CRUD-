from django import forms
from django.contrib.auth.models import User
from .models import Profile


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["__all__"]


class profileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()


class profileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
