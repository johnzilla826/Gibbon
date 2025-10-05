from django.shortcuts import render

def index(request):
    return render(request, "accounting/index.html")

def trial_balance(request):
    return render(request, "accounting/trial-balance.html")