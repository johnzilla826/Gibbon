from django.contrib import admin

from .models import Company, Account, Transaction, Split

admin.site.register(Company)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Split)

