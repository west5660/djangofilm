from django.db import models

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
        return self.name, self.spec

class Pacient(models.Model):
    name = models.CharField(max_length=40, verbose_name='Кличка пациента')
    adres = models.CharField(max_length=40, verbose_name='Адрес')
    tel = models.CharField(max_length=40, verbose_name='Телефон')

    def __str__(self):
        return self.name

class Zapisi(models.Model):
    num = models.IntegerField(verbose_name='Номер записи')
    pacient = models.ForeignKey(Pacient, on_delete=models.SET_NULL, null=True)
    spec = models.ManyToManyField(Spec)
    num_vizit = models.IntegerField()
    data_vizit = models.DateField(null=True, blank=False, verbose_name='Дата визита')
    anamnez = models.CharField(max_length=40, verbose_name='Анамнез')
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.SET_NULL, null=True)
    shema_lechenia = models.TextField(max_length=500, verbose_name='Схема лечения')
    chek_uslug = models.ForeignKey(Check, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.num

    # def display_pacient(self):
    #     res = ''
    #     for a in self.pacient.all():
    #         res += a.lname + ' '
    #     return res
    #
    # display_pacient.short_description = 'Пациенты'
