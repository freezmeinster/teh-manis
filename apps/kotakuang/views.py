from django.shortcuts import render_to_response 
from django.template import RequestContext
from kotakuang.forms import KategoriForm

def home(request):
    return render_to_response('kotakuang/index.html',{
	'url' : 'home',
	},context_instance=RequestContext(request))

def kategori(request):
    return render_to_response('kotakuang/kategori.html',{
	'url' : 'home',
	'form' : KategoriForm(),
	},context_instance=RequestContext(request))

def pemasukan(request):
    return render_to_response('kotakuang/index.html',{
	'url' : 'home',
	},context_instance=RequestContext(request))
	
def pengeluaran(request):
	return render_to_response('kotakuang/index.html',{
	    'url' : 'home',
	},context_instance=RequestContext(request))
    
def about(request):
    return render_to_response('kotakuang/about.html',{
	'url' : 'about',
	})