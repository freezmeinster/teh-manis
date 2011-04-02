from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    
    class Meta:
	verbose_name_plural = 'Daftar Kategori'
	verbose_name = 'Kategori'
	
    def __unicode__(self):
	return self.name

class Pengeluaran(models.Model):
    user = models.ForeignKey(User)
    nama = models.CharField(max_length=255)
    kategori = models.ForeignKey('Kategori')
    tgl_buat = models.DateTimeField(auto_now_add=True)
    jumlah = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
    keterangan = models.TextField(blank=True,null=True)
    
    class Meta:
	verbose_name_plural = 'Daftar Pemasukan'
	verbose_name = 'Pemasukan'
	
    def __unicode__(self):
	return self.name
    
class Pemasukan(models.Model):
    user = models.ForeignKey(User)
    nama = models.CharField(max_length=255)
    kategori = models.ForeignKey('Kategori')
    tgl_buat = models.DateTimeField(auto_now_add=True)
    jumlah = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
    keterangan = models.TextField(blank=True,null=True)
    
    class Meta:
	verbose_name_plural = 'Daftar Pemasukan'
	verbose_name = 'Pemasukan'
	
    def __unicode__(self):
	return self.name