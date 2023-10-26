from django.test import TestCase
from ..models import Currencies
from datetime import date

class TestModels(TestCase):
    def setUp(self):
        self.currency_record = Currencies(
            base_currency='EUR',
            quote_currency='PLN',
            open_rate=0.2232
        )
        self.currency_record.save()

    def test_open_rate_can_be_read(self):
        self.assertEquals(self.currency_record.open_rate, 0.2232)
        self.assertEquals(self.currency_record.currency_pair, "EURPLN")
        currency_str = str(self.currency_record)
        self.assertIn(date.today().strftime("%Y-%m-%d"), currency_str)

