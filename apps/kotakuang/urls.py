from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('kotakuang.views',
    

    url(r'^$', 'home', name="kotakuang_home"),
    url(r'^kategori/$', 'kategori', name="kotakuang_kategori"),
    url(r'^pemasukan/$', 'pemasukan', name="kotakuang_pengeluaran"),
    url(r'^pengeluaran/$', 'pengeluaran', name="kotakuang_pemasukan"),
    url(r'^about/$', 'about', name="kotakuang_about"),
)
