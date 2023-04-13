from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from wallet.models import Account, Transaction, Card, Wallet, Beneficiary


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['bank_name', 'account_number', 'amount']


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'phone', 'password', 'first_name', 'last_name']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'date']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_number', 'card_name', 'cvv', 'expiry_date']
        expiry_date = serializers.DateField(read_only=True)
