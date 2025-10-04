from django.urls import path

from . import views

app_name = "accounting"
urlpatterns = [
    path("/hello", views.index, name="index"),
]