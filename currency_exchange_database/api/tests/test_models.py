from django.test import TestCase
from ..models import CurrencyRates, Currencies
from datetime import date


class TestModels(TestCase):
    def setUp(self):
        base = Currencies(currency_code='EUR')
        base.save()
        quote = Currencies(currency_code='PLN')
        quote.save()

        self.currency_record = CurrencyRates(
            base_currency=base,
            quote_currency=quote,
            open_rate=0.2232
        )
        self.currency_record.save()

    def test_open_rate_can_be_read(self):
        self.assertEquals(self.currency_record.open_rate, 0.2232)
        self.assertEquals(f"{self.currency_record.base_currency.currency_code}{self.currency_record.quote_currency.currency_code}", "EURPLN")
        currency_str = str(self.currency_record)
        self.assertIn(date.today().strftime("%Y-%m-%d"), currency_str)

