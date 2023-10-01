from django.db import models
from django.urls import reverse
# Create your models here.
class Diagnoz(models.Model):
    diagnoz = models.CharField(max_length=40, verbose_name='Диагноз')

    def __str__(self):
        return self.diagnoz

class Check(models.Model):
    sum_mat= models.CharField(max_length=40, verbose_name='Материалы затраты')
    sum_uslug= models.CharField(max_length=40, verbose_name='Цена услуг')

    def __str__(self):
        return f'{self.sum_mat},{self.sum_uslug}'

class Spec(models.Model):
    name= models.CharField(max_length=40, verbose_name='Имя доктора')
    spec= models.CharField(max_length=40, verbose_name='Специальность доктора')

    def __str__(self):
        return f'{self.name},{self.spec}'

class Pacient(models.Model):
    name = models.CharField(max_length=40, verbose_name='Кличка пациента')
    adres = models.CharField(max_length=40, verbose_name='Адрес')
    tel = models.CharField(max_length=40, verbose_name='Телефон')

    def __str__(self):
        return self.name

class Zapisi(models.Model):
    num = models.CharField(max_length=40, verbose_name='Номер записи')
    pacient = models.ForeignKey(Pacient, on_delete=models.SET_NULL, null=True)
    spec = models.ManyToManyField(Spec)
    num_vizit = models.CharField(max_length=40, verbose_name='Номер визита')
    data_vizit = models.DateField(null=True, blank=False, verbose_name='Дата визита')
    anamnez = models.CharField(max_length=40, verbose_name='Анамнез')
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.SET_NULL, null=True)
    shema_lechenia = models.TextField(max_length=500, verbose_name='Схема лечения')
    chek_uslug = models.ForeignKey(Check, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.num

    def display_spec(self):
        res = ''
        for a in self.spec.all():
            res += a.name + ' '
        return res

    display_spec.short_description = 'Врач'

    def get_absolute_url(self):
        return reverse('info', args=[self.id])
