from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    # Main
    url(r'^$', 'index', name='main_index'),
    
)