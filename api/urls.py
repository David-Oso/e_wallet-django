from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('account', views.AccountCreateViewSet)
router.register('transaction', views.TransactionViewSet)
router.register('card', views.CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
