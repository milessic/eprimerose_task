from django.urls import path
from .views import Currency, CurrencyEurUsd

urlpatterns = [
    path('currency/', Currency.as_view(), name='currency'),
    path('currency/EUR/USD/', CurrencyEurUsd.as_view(), name='currency_eurusd'),
]