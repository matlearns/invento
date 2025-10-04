from django.urls import path
from .views import home, payment_accounts

urlpatterns = [
    path('', home, name='home'),
    path('payment_accounts', payment_accounts, name='payment_accounts')
]