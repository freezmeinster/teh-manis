from django.forms import ModelForm
from kotakuang.models import Kategori, Pemasukan,Pengeluaran

class KategoriForm(ModelForm):
    
    class Meta :
	model = Kategori