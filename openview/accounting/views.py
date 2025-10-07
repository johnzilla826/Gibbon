from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView

from .models import *
from .forms import CompanyForm, AccountForm


def index(request):
    return render(request, "accounting/index.html")


def trial_balance(request):
    return render(request, "accounting/reports/trial-balance.html")


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "accounting/create_view/create_company.html"
    success_url = "/accounting/"


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "accounting/create_view/create_account.html"
    success_url = "/accounting/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f"Account '{form.instance.name}' was created successfully!"
        )
        return response
