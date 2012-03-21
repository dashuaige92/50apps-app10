from django.db import models

# Create your models here.
class Stock(models.Model):
    """
    This class represents the stock object.
    """
    ticker = models.CharField(max_length=5)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
