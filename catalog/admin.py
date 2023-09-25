from atexit import register

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Genre)
# admin.site.register(Director)
# admin.site.register(Actor)
admin.site.register(AgeRate)
# admin.site.register(Status)
# admin.site.register(Kino)
admin.site.register(Country)


class Actoradmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'born', 'country')  # видимость таблицы в админке
    list_display_links = ('fname', 'lname')  # ссылка для перехода в карточку актера


admin.site.register(Actor, Actoradmin)  # регистрация модели актер и запуск ее работы


class Directoradmin(admin.ModelAdmin):
    list_display = ('fname', 'lname')
    list_display_links = ('fname', 'lname')


admin.site.register(Director, Directoradmin)


class Kinoadmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'display_actors')
    list_filter = ('status','genre','rating')                       #фильтр
    fieldsets = (('О Фильме',{'fields':('title','summary','actor')}),                     #какая то конструкция для карточки фильма
                 ('Рейтинг',{'fields':('rating','ager','status')}),
                 ('Остальное',{'fields':('genre','country','director','year')}))


admin.site.register(Kino, Kinoadmin)

class Stinline(admin.TabularInline):
    model = Kino

class Statusadmin(admin.ModelAdmin):
    inlines = [Stinline]
admin.site.register(Status,Statusadmin)
