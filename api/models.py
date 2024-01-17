from django.db import models


class CryptoCurrency(models.Model):
    cryptocurrency = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    market_cap = models.CharField(max_length=255)
    change = models.CharField(max_length=255)

    def __str__(self):
        return self.cryptocurrency
