from decimal import Decimal

from django.test import TestCase, Client
from django.urls import reverse
from urllib.error import HTTPError

from ..views import *


class TestsViews(TestCase):
    def test_currency_eur_usd_GET_200(self):
        client = Client()
        response = client.get(reverse('currency_eurusd'))
        self.assertEquals(response.status_code, 200)

    def test_currency_eur_usd_get_eurusd_200(self):
        eur_usd_result = CurrencyEurUsd().get_eurusd()
        rate = getattr(eur_usd_result, 'open_rate')
        self.assertIsInstance(rate, Decimal)
        self.assertEquals(rate, round(rate, 5))