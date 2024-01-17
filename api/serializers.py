from rest_framework import serializers

from .models import CryptoCurrency


class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ['cryptocurrency', 'price', 'market_cap', 'change']
