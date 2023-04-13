from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from wallet.models import Account


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['bank_name', 'account_number', 'amount']


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['username', 'email', 'phone', 'password', 'first_name', 'last_name']
