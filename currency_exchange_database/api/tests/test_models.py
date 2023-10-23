from django.test import TestCase
from ..models import EurUsdCurrencies


class TestModels(TestCase):
    def setUp(self):
        self.currency_record = EurUsdCurrencies.objects.create(
            open_rate=9.0598,
            utc_timestamp="2023-10-23T09:19:28.703092Z"
        )

    def test_open_rate_can_be_read(self):
        self.assertEquals(self.currency_record.open_rate, 9.0598)