from django.urls import path

from . import views
from .views import CompanyCreateView

app_name = "accounting"
urlpatterns = [
    path("", views.index, name="index"),
    path("reports/trial-balance/", views.trial_balance, name="trial-balance"),
    path("company/new", CompanyCreateView.as_view(), name="company_create")
]