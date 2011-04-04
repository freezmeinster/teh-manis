from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response 
from django.template.defaultfilters import slugify
from django.template import RequestContext
from kotakuang.forms import KategoriForm,PengeluaranForm,PemasukanForm
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
        data['slug'] = slugify(data['nama'])
        form = KategoriForm(data)
        if form.is_valid():
            form.save()
    
    return render_to_response('kotakuang/kategori.html',{
    'url' : 'kategori',
    'kategori' : kategori,
    'form' : KategoriForm(),
    },context_instance=RequestContext(request))

def pemasukan(request):
    pemasukan = Pemasukan.objects.filter(user=request.user).order_by('tgl_buat').reverse()
    paginator = Paginator(pemasukan, 6)
    page = int(request.GET.get('page', '1'))
    # If page request (9999) is out of range, deliver last page of results.
    try:
        post_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        post_page = paginator.page(paginator.num_pages)
    
    if request.method == 'POST' :
        data = request.POST.copy()
        data['user'] = request.user.id
        form  = PemasukanForm(data)
        if form.is_valid():
            form.save()
            
    return render_to_response('kotakuang/pemasukan.html',{
        'url' : 'pemasukan',
        'pemasukan' : post_page,
        'form' : PemasukanForm(),
    },context_instance=RequestContext(request))
    
def pengeluaran(request):
    pengeluaran = Pengeluaran.objects.filter(user=request.user).order_by('tgl_buat').reverse()
    
    paginator = Paginator(pengeluaran, 6)
    page = int(request.GET.get('page', '1'))
    # If page request (9999) is out of range, deliver last page of results.
    try:
        post_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        post_page = paginator.page(paginator.num_pages)
    
    if request.method == 'POST' :
        data = request.POST.copy()
        data['user'] = request.user.id
        data['total'] = int(data['jumlah']) * int(data['harga'])
        form = PengeluaranForm(data)
        if form.is_valid():
            form.save()
    
    return render_to_response('kotakuang/pengeluaran.html',{
        'url' : 'pengeluaran',
        'pengeluaran' : post_page,
        'form' : PengeluaranForm,
    },context_instance=RequestContext(request))
    
def about(request):
    return render_to_response('kotakuang/about.html',{
    'url' : 'about',
    },context_instance=RequestContext(request))
