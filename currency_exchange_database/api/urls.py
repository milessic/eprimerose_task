from django.urls import path
from .views import Currency, CurrencyEurUsd

urlpatterns = [
    path('currency/', Currency.as_view()),
    path('currency/EUR/USD/', CurrencyEurUsd.as_view()),
]