from django.db import models


class EurUsdCurrencies(models.Model):
    # open_rate - open rate from given query,
    # utc_timestamp - DateTime timestamp for UTC timezone
    open_rate = models.DecimalField(max_digits=10, decimal_places=4)
    utc_timestamp = models.DateTimeField(auto_now_add=True)

