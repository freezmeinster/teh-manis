from django.shortcuts import render_to_response 

def home(request):
    return render_to_response('kotakuang/index.html',{
	'url' : 'home',
    })
    
def about(request):
    return render_to_response('kotakuang/about.html',{
	'url' : 'about',
	})