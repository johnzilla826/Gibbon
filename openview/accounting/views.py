from django.shortcuts import render

def index(request):
    return render(request, "accounting/index.html")

def trial_balance(request):
    return render(request, "accounting/reports/trial-balance.html")

def create_entry(request):
    return render(request, "accounting/create-entry.html")