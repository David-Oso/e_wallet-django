from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(unique=True, max_length=11, blank=False, null=False)

    def __str__(self):
        return self.first_name


class Account(models.Model):
    bank_name = models.CharField(max_length=255, blank=False, null=False)
    account_number = models.CharField(max_length=10, blank=False, null=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.bank_name


class Card(models.Model):
    card_number = models.CharField(max_length=16, blank=False, null=False)
    card_name = models.CharField(max_length=255, blank=False, null=False)
    cvv = models.CharField(max_length=3, blank=False, null=False)
    expiry_date = models.DateField()

    def __str__(self):
        return self.card_name


class Beneficiary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
