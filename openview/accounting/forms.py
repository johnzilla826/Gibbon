from django import forms
from .models import Company

class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "location"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }