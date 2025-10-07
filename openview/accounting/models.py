from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    ACCOUNT_TYPES = [
        ("ASSET", "Asset"),
        ("LIABILITY", "Liability"),
        ("EQUITY", "Equity"),
        ("INCOME", "Income"),
        ("EXPENSE", "Expense"),
    ]

    classification = models.CharField(choices=ACCOUNT_TYPES)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.name}"


class Transaction(models.Model):
    date = models.DateField()
    memo = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.memo}"


class Split(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)

    debit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return f"Transaction #{self.transaction.id} --- Debit: {self.debit}, Credit: {self.credit}"
