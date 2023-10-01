from django.shortcuts import render
from .models import *
# Create your views here.

def index(req):
    numkino = Pacient.objects.all().count()
    numactor = Spec.objects.all().count()
    numfree = Diagnoz.objects.all().count()
    data = {'k1': numkino, 'k2': numactor, 'k3': numfree}
    return render(req, 'index.html', context=data)

def allkino(req):

    return render(req,'index.html')

from django.views import generic
class Kinolist(generic.ListView):
    model = Pacient

class KinoDetail(generic.DetailView):
    model = Pacient

# from django.http import HttpResponse
# def info(req,id):
#     film = Kino.objects.get(id=id)
#     return HttpResponse(film.title)