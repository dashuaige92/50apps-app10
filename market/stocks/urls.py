urlpatterns = patterns('stocks.views',
     url(r'^dashboard/', 'dashboard'),
     url(r'^api/', 'ajax_stocks'),
     
)
