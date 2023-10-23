from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import *


class TestUrls(SimpleTestCase):
    def test_currency_url_is_resovled(self):
        url = reverse('currency')
        self.assertEquals(resolve(url).func.view_class, Currency)

    def test_currency_eurusd_url_is_resovled(self):
        url = reverse('currency_eurusd')
        self.assertEquals(resolve(url).func.view_class, CurrencyEurUsd)
