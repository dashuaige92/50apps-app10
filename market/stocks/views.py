# Create your views here.
import simplejson as json

from django.shortcuts import render_to_response
from django.http import HttpResponse

from stocks.models import Stock

def dashboard(request):
    stocks = Stock.objects.all()
    return render_to_response('index.html', {
        'stocks': stocks
    })

def ajax_stocks(request):
    response = json.dumps(Stock.objects.all())
    return HttpResponse(response)
