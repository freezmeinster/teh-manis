from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('kotakuang.views',
    

    url(r'^$', 'home', name="kotakuang_home"),
    url(r'^about/$', 'about', name="kotakuang_about"),
    url(r'^login/?$', 'login', name="kotakuang_login"),
    url(r'^register/?$', 'register', name="kotakuang_daftar"),
)
