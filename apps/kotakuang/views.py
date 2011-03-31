from django.shortcuts import render_to_response 
from django.template import RequestContext

def login(request):
    return render_to_response('kotakuang/login.html',{
	'url' : 'home',
	},context_instance=RequestContext(request))
	

def register(request):
    return render_to_response('kotakuang/register.html',{
	'url' : 'home',
	})

def home(request):
    return render_to_response('kotakuang/index.html',{
	'url' : 'home',
	},context_instance=RequestContext(request))
    
def about(request):
    return render_to_response('kotakuang/about.html',{
	'url' : 'about',
	})