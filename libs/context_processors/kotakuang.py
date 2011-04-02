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
