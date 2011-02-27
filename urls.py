from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # Login & logout
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}, name="auth_login"),
    
    # Project apps
    (r'^', include('main.urls')),
    
    # 3rd party apps
    
    # Robots
    (r'^robots.txt$', include('robots.urls')),
)
