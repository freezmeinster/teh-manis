from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    user = models.ForeignKey(User) 
    
    class Meta:
	verbose_name_plural = 'Daftar Kategori'
	verbose_name = 'Kategori'
	
    def __unicode__(self):
	return self.nama

class Pengeluaran(models.Model):
    user = models.ForeignKey(User)
    nama = models.CharField(max_length=255)
    kategori = models.ForeignKey('Kategori')
    tgl_buat = models.DateTimeField(auto_now_add=True)
    jumlah = models.PositiveIntegerField()
    harga = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    keterangan = models.TextField(blank=True,null=True)
    
    class Meta:
	verbose_name_plural = 'Daftar Pengeluaran'
	verbose_name = 'Pengeluaran'
	
    def __unicode__(self):
	return self.nama
    
class Pemasukan(models.Model):
    user = models.ForeignKey(User)
    nama = models.CharField(max_length=255)
    kategori = models.ForeignKey('Kategori')
    tgl_buat = models.DateTimeField(auto_now_add=True)
    jumlah = models.PositiveIntegerField()
    keterangan = models.TextField(blank=True,null=True)
    
    class Meta:
	verbose_name_plural = 'Daftar Pemasukan'
	verbose_name = 'Pemasukan'
	
    def __unicode__(self):
	return self.nama
