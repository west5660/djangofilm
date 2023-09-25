from atexit import register

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Diagnoz)
admin.site.register(Check)
admin.site.register(Spec)
admin.site.register(Pacient)
admin.site.register(Zapisi)
# admin.site.register(Kino)
# admin.site.register(Country)

# class Diagnozadmin(admin.ModelAdmin):
#     list_display_links = ('diagnoz')
# admin.site.register(Diagnoz,Diagnozadmin)
#
# class Checkadmin(admin.ModelAdmin):
#     list_display = ('sum_mat','sum_uslug')
# admin.site.register(Check,Checkadmin)
#
# class Specadmin(admin.ModelAdmin):
#     list_display_links = ('name','spec')
# admin.site.register(Spec,Specadmin)
#
# class Pacientadmin(admin.ModelAdmin):
#     list_display_links = ('name', 'adres', 'tel')
# admin.site.register(Pacient,Pacientadmin)

