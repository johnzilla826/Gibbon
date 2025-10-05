from django.urls import path

from . import views

app_name = "accounting"
urlpatterns = [
    path("", views.index, name="index"),
    path("reports/trial-balance/", views.trial_balance, name="trial-balance"),
    path("create-entry/", views.create_entry, name="create-entry")
]