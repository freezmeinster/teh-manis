from django.shortcuts import render_to_response 
from django.template import RequestContext
from kotakuang.forms import KategoriForm,PengeluaranForm
from kotakuang.models import Kategori,Pengeluaran,Pemasukan

def home(request):
    return render_to_response('kotakuang/index.html',{
	'url' : 'home',
	},context_instance=RequestContext(request))

def kategori(request):
    kategori = Kategori.objects.filter(user=request.user)
    
    if request.method == 'POST' :
	data = request.POST.copy()
	data['user'] = request.user.id
	form = KategoriForm(data)
	if form.is_valid():
	    form.save()
    
    return render_to_response('kotakuang/kategori.html',{
	'url' : 'kategori',
	'kategori' : kategori,
	'form' : KategoriForm(),
	},context_instance=RequestContext(request))

def pemasukan(request):
    return render_to_response('kotakuang/index.html',{
	'url' : 'pemasukan',
	},context_instance=RequestContext(request))
	
def pengeluaran(request):
	pengeluaran = Pengeluaran.objects.filter(user=request.user)
	if request.method == 'POST' :
	    data = request.POST.copy()
	    data['user'] = request.user.id
	    data['total'] = int(data['jumlah']) * int(data['harga'])
	    form = PengeluaranForm(data)
	    if form.is_valid():
		form.save()
	
	return render_to_response('kotakuang/pengeluaran.html',{
	    'url' : 'pengeluaran',
	    'pengeluaran' : pengeluaran,
	    'form' : PengeluaranForm,
	},context_instance=RequestContext(request))
    
def about(request):
    return render_to_response('kotakuang/about.html',{
	'url' : 'about',
	},context_instance=RequestContext(request))