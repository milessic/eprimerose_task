from django.db import models


class Currencies(models.Model):
    base_currency = models.CharField(max_length=3)
    quote_currency = models.CharField(max_length=3)
    open_rate = models.DecimalField(max_digits=10, decimal_places=4)
    utc_timestamp = models.DateTimeField(auto_now_add=True)
    currency_pair = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.currency_pair} - {str(self.utc_timestamp)[:19]}'

    def save(self, *args, **kwargs):
        # overriding save method to
        self.base_currency = self.base_currency.upper()
        self.quote_currency = self.quote_currency.upper()
        self.currency_pair = f"{self.base_currency}{self.quote_currency}"
        super(Currencies, self).save(*args, **kwargs)

