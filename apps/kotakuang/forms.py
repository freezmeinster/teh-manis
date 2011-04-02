from django.forms import ModelForm
from kotakuang.models import Kategori, Pemasukan,Pengeluaran

class KategoriForm(ModelForm):
    
    class Meta :
		model = Kategori
	

class PengeluaranForm(ModelForm):
    
    class Meta :
		model = Pengeluaran

class PemasukanForm(ModelForm):
	
	class Meta :
		model = Pemasukan
