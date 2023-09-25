from atexit import register

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Diagnoz)
# admin.site.register(Check)
# admin.site.register(Spec)
# admin.site.register(Pacient)
# admin.site.register(Zapisi)
# admin.site.register(Kino)
# admin.site.register(Country)

# class Diagnozadmin(admin.ModelAdmin):
#     list_display = ('diagnoz')
# admin.site.register(Diagnoz,Diagnozadmin)
#
class Checkadmin(admin.ModelAdmin):
    list_display = ('sum_mat','sum_uslug')
admin.site.register(Check,Checkadmin)

class Specadmin(admin.ModelAdmin):
    list_display = ('name','spec')
admin.site.register(Spec,Specadmin)

class Pacientadmin(admin.ModelAdmin):
    list_display = ('name', 'adres', 'tel')
admin.site.register(Pacient,Pacientadmin)

class Zapisiadmin(admin.ModelAdmin):
    list_display = ('num', 'pacient','display_spec', 'data_vizit', 'diagnoz')
    list_filter = ('pacient', 'data_vizit', 'diagnoz')  # фильтр
    fieldsets = (('О приеме', {'fields': ('anamnez', 'shema_lechenia', 'chek_uslug','pacient','spec')}),  # какая то конструкция для карточки фильма
                 ('Визит', {'fields': ('num_vizit', 'data_vizit','num','diagnoz')}))


admin.site.register(Zapisi, Zapisiadmin)

