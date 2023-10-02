from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.

def index(req):
    numkino = Kino.objects.all().count()
    numactor = Actor.objects.all().count()
    numfree = Kino.objects.filter(status__kino=1).count()
    try:
        username = req.user.username
    except:
        username = 'Гость'
    username = req.user.username
    data = {'k1':numkino, 'k2':numactor, 'k3':numfree, 'username':username}
    # user = User.objects.create_user('user2','user2@mail.ru','useruser')
    # user.first_name = 'Vlad'
    # user.last_name = 'Petrov'
    # user.save()
    return render(req,'index.html', context=data)

# def allkino(req):
#
#     return render(req,'index.html')

from django.views import generic
class Kinolist(generic.ListView):
    model = Kino
    paginate_by = 2
class KinoDetail(generic.DetailView):
    model = Kino
class Actorlist(generic.ListView):
    model = Actor
    paginate_by = 2
class ActorDetail(generic.DetailView):
    model = Actor

class Directorlist(generic.ListView):
    model = Director
    paginate_by = 2
class DirectorDetail(generic.DetailView):
    model = Director
# from django.http import HttpResponse
# def info(req,id):
#     film = Kino.objects.get(id=id)
#     return HttpResponse(film.title)