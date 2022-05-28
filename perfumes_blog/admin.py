from django.contrib import admin
from . models import Perfume
# Register your models here.

class AdminPerfume(admin.ModelAdmin):
    list_display = ['perfume_name', 'purchaser', 'date_updated']

admin.site.register(Perfume, AdminPerfume)