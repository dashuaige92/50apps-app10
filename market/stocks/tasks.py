import random
from celery.task import task

from stocks.models import Stock

@task
def modify_prices():
    max_change = .05
    for stock in Stock.objects.all():
        stock.current_price += random.triangular(-max_change * stock.current_price,
                max_change * stock.current_price)
        stock.save()
