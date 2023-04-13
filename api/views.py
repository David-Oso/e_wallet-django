from rest_framework.viewsets import ModelViewSet

from api.serializers import AccountCreateSerializer
from wallet.models import Account


# Create your views here.
class AccountCreateViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
