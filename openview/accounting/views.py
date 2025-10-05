from django.shortcuts import render
from django.views.generic import CreateView

from .models import *
from .forms import CreateCompanyForm

def index(request):
    return render(request, "accounting/index.html")

def trial_balance(request):
    return render(request, "accounting/reports/trial-balance.html")

class CompanyCreateView(CreateView):
    model = Company
    form_class = CreateCompanyForm
    template_name = "accounting/create_view/create_company.html"
    success_url = "/accounting/"