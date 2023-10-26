from django.urls import path
from .views import Currency, CurrencyConverter

urlpatterns = [
    path('currency/', Currency.as_view(), name='currency'),
    path('currency/<str:base>/<str:quote>/', CurrencyConverter.as_view(), name='currency_rate'),
]