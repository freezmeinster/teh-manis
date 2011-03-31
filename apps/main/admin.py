from django.contrib import admin
from main import models

admin.site.register(models.Post)
admin.site.register(models.Kategori)
admin.site.register(models.Tamu)
admin.site.register(models.Quote)