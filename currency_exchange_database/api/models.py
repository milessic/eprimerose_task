from django.db import models


class Currencies(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    def __str__(self):
        return self.currency_code


class CurrencyRates(models.Model):
    base_currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, related_name="base")
    quote_currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, related_name="quote")
    open_rate = models.DecimalField(max_digits=10, decimal_places=4)
    utc_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.base_currency}{self.quote_currency} - {str(self.utc_timestamp)[:19]}'

    def save(self, *args, **kwargs):
        # overriding save method to
        # self.base_currency = self.base_currency.upper()
        # self.quote_currency = self.quote_currency.upper()
        super(CurrencyRates, self).save(*args, **kwargs)

