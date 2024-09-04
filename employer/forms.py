from django import forms


class EmployerForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField(max_length=120)
