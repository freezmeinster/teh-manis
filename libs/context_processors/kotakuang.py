from apps.kotakuang.models import Kategori,Pengeluaran,Pemasukan

def user( request ):
    total = long()
    if request.user.is_anonymous()  :
	pass
    else :
	pengeluaran = Pengeluaran.objects.filter(user=request.user)
	for data in pengeluaran :
	    total = data.total + total
	
    return { 'total_pengeluaran' : total  }