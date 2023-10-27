from rest_framework import serializers
from .models import CurrencyRates, Currencies
from django.forms import ValidationError


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ('currency_code',)


class CurrencyRatesSerializer(serializers.ModelSerializer):
    base_currency = CurrencySerializer().fields['currency_code']
    quote_currency = CurrencySerializer().fields['currency_code']

    class Meta:
        model = CurrencyRates
        fields = "__all__"

    def validate(self, data):
        if len(data['base_currency']) != 3 or (data['quote_currency']) != 3 :
            raise ValidationError("Each currency code has to be 3 digits code.")
        return value
