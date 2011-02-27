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
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}, name="auth_login"),
    
    # Password reset
    #url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'registration/password_reset.html', 'email_template_name': 'registration/password_reset_email.html'}),
    #url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'registration/password_reset_done.html'}),
    #url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'registration/password_reset_confirm.html'}),
    #url(r'^accounts/password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'registration/password_reset_complete.html',}),
    
    # Project apps
    (r'^', include('main.urls')),
    
    # 3rd party apps
    
    # Robots
    (r'^robots.txt$', include('robots.urls')),
)
