from django.contrib import admin

from wallet.models import Wallet, User, Transaction, Card


# Register your models here.


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'account']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'date']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['card_number', 'card_name', 'cvv', 'expiry_date']
