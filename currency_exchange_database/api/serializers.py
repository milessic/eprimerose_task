from rest_framework import serializers
from .models import EurUsdCurrencies


class EurUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = EurUsdCurrencies
        fields = '__all__'
