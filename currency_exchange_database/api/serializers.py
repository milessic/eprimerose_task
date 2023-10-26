from rest_framework import serializers
from .models import Currencies
from django.forms import ValidationError


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'

    def validate(self, data):
        if len(data['base_currency']) != 3 or (data['quote_currency']) != 3 :
            raise ValidationError("Each currency code has to be 3 digits code.")
        return value

