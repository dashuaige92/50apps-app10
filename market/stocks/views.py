# Create your views here.
from decimal import *
import random, string
import json

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from stocks.models import Stock
from stocks.tasks import *

def dashboard(request):
    stocks = Stock.objects.all()
    return render_to_response('index.html', {
        'stocks': stocks
    }, context_instance=RequestContext(request))

def ajax_stocks(request):
    modify_stocks(request)
    
    response = json.dumps({
        s.ticker : float(s.current_price) for s in Stock.objects.all().order_by('ticker')})
    return HttpResponse(response)

def generate_stocks(request):
    Stock.objects.all().delete()
    for i in xrange(20):
        s = Stock()
        s.ticker = ''.join(random.choice(string.uppercase) for x in xrange(random.randint(3, 4)))
        s.current_price = Decimal.from_float(random.triangular(0, 1000, 0)).quantize(Decimal('.01'))
        s.save()
    
    return HttpResponseRedirect(reverse('stocks.views.dashboard'))

def modify_stocks(request):
    max_change = Decimal('.05')
    for stock in filter(lambda s: s.current_price, Stock.objects.all()):
        stock.current_price = max(0, stock.current_price + Decimal(random.triangular(-10, 10)))
        stock.save()
