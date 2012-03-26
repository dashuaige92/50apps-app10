from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('stocks.views',
     url(r'^$', 'dashboard'),
     url(r'^api$', 'ajax_stocks'),
     url(r'^api/generate$', 'generate_stocks'),
     url(r'^api/modify$', 'modify_stocks'),
     
)
