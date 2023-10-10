from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
# Create your views here.

def index(req):
    numkino = Kino.objects.all().count()
    numactor = Actor.objects.all().count()
    numfree = Kino.objects.filter(status__kino=1).count()
    if req.user.username:
        username=req.user.first_name
        # print(req.user.first_name, '#', req.user.id)
    else:
        username='Гость'
        print(req.user.id)
    # username = req.user.username
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

def status(req):
    k1 = Status.objects.all()
    data = {'podpiska':k1}
    return render(req,'podpiska.html', data)

def prosmotr(req,id1,id2,id3):
    print(id1,id2,id3)
    mas=['бесплатно','базовая','супер'] #kino id2
    mas2=['free','based','super']    #user   id3
    if id3!=0:
        status = User.objects.get(id=id3)  # нашли юзера
        print(status)
        status = status.groups.all()   #нашли его подписки
        status = status[0].id       #нашли айди его подписки
        print(status)
    if id3==0:                  #выдает гостю подписку номер 1
        status=1
    if status>=id2:             #сравниваем может ли он смотреть этот фильм
        print('ok')
        permission = True
    else:
        print('nelza')
        permission = False

    k1=Kino.objects.get(id=id1).title
    k2=Group.objects.get(id=status).name
    k3=Status.objects.get(id=id2).name
    data = {'kino':k1,'status':k2,'statuskino':k3, 'prava':permission}
    return render(req, 'prosmotr.html',data)

def buy(req,type):
    usid=req.user.id                    #находим текущего пользователя
    user123=User.objects.get(id=usid)      #находим в таблице user
    statusnow=user123.groups.all()[0].id    #номер его подписки(группы)
    grold=Group.objects.get(id=statusnow)      #нашли группу в таблице group
    grold.user_set.remove(user123)             #удалили из группы
    grnew=Group.objects.get(id=type)           #находим новую подписку
    grnew.user_set.add(user123)                 # выписываем новую подписку
    k1=grnew.name
    data={'podpiska':k1}
    return render(req,'buy.html',data)