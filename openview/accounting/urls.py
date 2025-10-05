from django.urls import path

from . import views
from .views import CompanyCreateView, AccountCreateView

app_name = "accounting"
urlpatterns = [
    path("", views.index, name="index"),
    path("reports/trial-balance/", views.trial_balance, name="trial-balance"),
    path("company/new", CompanyCreateView.as_view(), name="company_create"),
    path("account/new", AccountCreateView.as_view(), name="account_create"),
]
