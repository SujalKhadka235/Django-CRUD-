from django import forms
from .models import Person


class EmployeeForm(forms.ModelForm):
    address = forms.CharField(max_length=20)

    class Meta:
        model = Person
        fields = ["first_name", "last_name"]
