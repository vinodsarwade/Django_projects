from django.db import models

# Create your models here.
class Stock(models.Model):
    stockName = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.stockName