from rest_framework.viewsets import ModelViewSet

from api.serializers import AccountCreateSerializer, TransactionSerializer, CardSerializer
from wallet.models import Account, Transaction, Card


# Create your views here.
class AccountCreateViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
