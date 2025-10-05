from django import forms
from .models import *

class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "location"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }
        
class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["number", "name", "description", "company", "classification", "parent"]
        widgets = {
            "number": forms.NumberInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.Select(attrs={"class": "form-control"}),
            "classification": forms.Select(attrs={"class": "form-control"}),   
            "parent": forms.Select(attrs={"class": "form-control"}),
		}