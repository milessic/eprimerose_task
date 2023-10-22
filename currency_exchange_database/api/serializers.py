from rest_framework import serializers
from .models import Currencies

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'