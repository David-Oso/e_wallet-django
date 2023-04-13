from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('wallet', views.AccountCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
