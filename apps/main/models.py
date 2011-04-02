from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    
    class Meta:
	verbose_name_plural = 'Daftar Kategori'
	verbose_name = 'Kategori'
    
    def __unicode__(self):
        return self.nama

class Post(models.Model):
    
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    tgl_buat = models.DateTimeField(auto_now_add=True)
    kategori = models.ForeignKey('Kategori')
    
    class Meta:
	verbose_name_plural = 'Daftar Posting'
	verbose_name = 'Post'

    def __unicode__(self):
        return self.judul
        
class Tamu(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    web = models.CharField(max_length=255)
    telp = models.CharField(max_length=255)
    tgl_daftar = models.DateTimeField(auto_now_add=True)
    
    class Meta:
	verbose_name_plural = 'Daftar Tamu'
	verbose_name = 'Tamu'
    
    def __unicode__(self):
        return "Pengunjung %s " % self.nama
       
class Quote(models.Model):
    author = models.CharField(max_length=255)
    isi = models.TextField()
    tgl_buat = models.DateTimeField(auto_now_add=True)
    
    class Meta:
	verbose_name_plural = 'Daftar Quote'
	verbose_name = 'Quote'
	ordering = ['tgl_buat']
    
    def __unicode__(self):
	return self.isi