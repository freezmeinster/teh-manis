from apps.kotakuang.models import Kategori,Pengeluaran,Pemasukan

def user( request ):
    total = long()
    masuk = long()
    saldo = long()
    if request.user.is_anonymous()  :
	pass
    else :
	pengeluaran = Pengeluaran.objects.filter(user=request.user)
	pemasukan = Pemasukan.objects.filter(user=request.user)
	for data in pengeluaran :
	    total = data.total + total
	
	for data in pemasukan :
		masuk = data.jumlah + masuk
	
    return { 
		'total_pengeluaran' : total,
		'total_pemasukan' : masuk,
		'saldo' : masuk - total,
		}

def acounting( request ):
    total = long()
    masuk = long()
    keluar = Pengeluaran.objects.filter(user=request.user)
    pemasukan = Pemasukan.objects.filter(user=request.user)
    awal = keluar[0]
    akhir = keluar.latest('tgl_buat')
    rentang = akhir.tgl_buat.toordinal() - awal.tgl_buat.toordinal()
    
    for data in pemasukan :
	masuk = data.jumlah + masuk
    
    for data in keluar:
	total = data.total + total
    saldo = masuk - total
    rata = int(total) / int(rentang+1)
    hidup = saldo / rata
    
    
    return {
	'perhari' : rata,
	'hidup' : hidup
    }