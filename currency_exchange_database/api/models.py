from django.db import models


class Currencies(models.Model):
    amount = models.DecimalField()
    currency = models.CharField(max_length=3)
    currency_to_eur = models.DecimalField(decimal_places=2)
    eur_to_usd = models.DecimalField(decimal_places=4)
    utc_timestamp = models.DateTimeField(auto_now_add=True)
