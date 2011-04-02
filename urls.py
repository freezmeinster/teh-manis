from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)), 
    (r'^kotakuang/',include('kotakuang.urls')),

    url('^$', 'main.views.home',name="main"),
)

urlpatterns += patterns('',
    url('^register/(?P<apps_id>\d+)$', 'main.views.register',name="register"),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', 
	    {'next_page': '/',},name='user_logout'),
    url(r'^login/?$', 'django.contrib.auth.views.login',
    { 'authentication_form': AuthenticationForm, 'template_name': 'main/login.html'},name='user_login'),
)