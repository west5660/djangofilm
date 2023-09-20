from django.db import models

# Create your models here.
class Diagnoz(models.Model):
    diagnoz = models.CharField(max_length=40)

    def __str__(self):
        return self.diagnoz

class Check(models.Model):
    sum_mat= models.CharField(max_length=40)
    sum_uslug= models.CharField(max_length=40)

    def __str__(self):
        return self.sum_uslug

class Spec(models.Model):
    name= models.CharField(max_length=40)
    spec= models.CharField(max_length=40)

    def __str__(self):
        return self.name, self.spec

class Pacient(models.Model):
    name = models.CharField(max_length=40)
    adres = models.CharField(max_length=40)
    tel = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Zapisi(models.Model):
    num = models.IntegerField()
    pacient = models.ForeignKey(Pacient, on_delete=models.SET_NULL, null=True)
    spec = models.ManyToManyField(Spec)
    num_vizit = models.IntegerField()
    data_vizit = models.DateField(null=True, blank=False)
    anamnez = models.CharField(max_length=40)
    diagnoz = models.ForeignKey(Diagnoz, on_delete=models.SET_NULL, null=True)
    shema_lechenia = models.TextField(max_length=500)
    chek_uslug = models.ForeignKey(Check, on_delete=models.SET_NULL, null=True)
