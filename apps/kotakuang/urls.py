from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('kotakuang.views',
    url(r'^$', 'home', name="kotakuang_home"),

)
