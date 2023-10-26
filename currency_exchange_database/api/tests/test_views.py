from decimal import Decimal

from django.test import TestCase, Client
from django.urls import reverse

from random import randint
from ..views import *


class TestViewsCurrency(TestCase):
    def setUp(self):
        for i in range(20):
            Currencies.objects.create(open_rate=f"{randint(0, 2)}.{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}",
                                      utc_timestamp=f"2023-0{randint(0,9)}-{randint(0,2)}{randint(0,9)}T09:19:{randint(0,5)}{randint(0,9)}.703092Z")
    def test_currency_GET_200(self):
        client = Client()
        response = client.get(reverse('currency'))
        self.assertEquals(response.status_code, 200)

    def test_currency_GET_check_default_order_is_DESC(self):
        client = Client()
        response = client.get(f"""{reverse('currency')}""")
        self.assertEquals(response.status_code, 200)
        first_iteration = True
        for key in response.data:
            if not first_iteration:
                self.assertTrue(key['id'] < previous_id)
            else:
                first_iteration = False
            previous_id = key['id']

    def test_currency_GET_check_order_is_ASC(self):
        client = Client()
        response = client.get(f"""{reverse('currency')}?order=ASC""")
        self.assertEquals(response.status_code, 200)
        first_iteration = True
        for key in response.data:
            if first_iteration:
                first_iteration = False
            else:
                self.assertTrue(key['id'] > previous_id)
            previous_id = key['id']

    def test_currency_GET_check_order_unsupported_value_is_DESC(self):
        client = Client()
        response = client.get(f"""{reverse('currency')}?order=pink_penguin""")
        self.assertEquals(response.status_code, 200)
        first_iteration = True
        for key in response.data:
            if first_iteration:
                first_iteration = False
            else:
                self.assertTrue(key['id'] < previous_id)
            previous_id = key['id']

    def test_currency_GET_check_limit(self):
        client = Client()
        limit = 3
        response = client.get(f"""{reverse('currency')}?limit={limit}""")
        self.assertEquals(response.status_code, 200)
        key_count = len(response.data)
        self.assertTrue(key_count == limit)

    def test_currency_GET_check_limit_higher_than_actual(self):
        client = Client()
        response = client.get(reverse('currency'))
        self.assertEquals(response.status_code, 200)
        key_count = len(response.data)
        response_2 = client.get(f"""{reverse('currency')}?limit={key_count+10}""")
        key_count_2 = len(response.data)
        self.assertTrue(key_count_2 == key_count)


class TestsViewsCurrencyEurUsd(TestCase):
    def test_currency_eur_usd_GET_200(self):
        client = Client()
        response = client.get(reverse('currency_rate', args=("EUR", "USD")))
        self.assertEquals(response.status_code, 200)

    def test_currency_converter_get_rate_200(self):
        eur_usd_result = CurrencyConverter().get_rate("EUR", "PLN")
        rate = getattr(eur_usd_result, 'open_rate')
        self.assertIsInstance(rate, Decimal)
        self.assertEquals(rate, round(rate, 5))

