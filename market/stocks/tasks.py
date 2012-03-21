import random
from celery.task import task

from stocks.models import Stock

@task
def modify_prices():
    max_change = Decimal('.05')
    for stock in Stock.objects.all():
        #stock.current_price += Decimal(random.triangular(-max_change * stock.current_price,
        stock.current_price += Decimal(random.triangular(-10, 10))
        stock.save()
