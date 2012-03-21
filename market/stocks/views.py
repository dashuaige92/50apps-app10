# Create your views here.
from decimal import *
import random, string
import json

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from stocks.models import Stock

def dashboard(request):
    stocks = Stock.objects.all()
    return render_to_response('index.html', {
        'stocks': stocks
    }, context_instance=RequestContext(request))

def ajax_stocks(request):
    response = json.dumps({
        s.ticker : float(s.current_price) for s in Stock.objects.all()})
    return HttpResponse(response)

def generate_stocks(request):
    Stock.objects.all().delete()
    for i in xrange(20):
        s = Stock()
        s.ticker = ''.join(random.choice(string.uppercase) for x in xrange(4))
        s.current_price = Decimal.from_float(random.triangular(0, 1000, 0)).quantize(Decimal('.01'))
        s.save()
    
    return HttpResponseRedirect('/stocks/')
    #return HttpResponseRedirect(reverse('/stocks/'))
