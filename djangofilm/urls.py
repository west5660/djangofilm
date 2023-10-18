"""
URL configuration for djangofilm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import myapp as myapp
from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('kino/',views.Kinolist.as_view(), name='allkino'),
    path('actor/',views.Actorlist.as_view(), name='allactor'),
    path('director/',views.Directorlist.as_view(), name='alldirector'),
    # path('kino/<int:id>/',views.info, name='info'),
    path('kino/<slug:pk>/<str:title>',views.KinoDetail.as_view(), name='info'),
    path('actor/<slug:pk>/<str:title>',views.ActorDetail.as_view(), name='infoactor'),
    path('director/<slug:pk>/<str:title>',views.DirectorDetail.as_view(), name='infodirector'),
    path('user/', include('django.contrib.auth.urls')),
    path('status/',views.status,name='status'),
    path('status/prosmotr/<int:id1>/<int:id2>/<int:id3>',views.prosmotr,name='prosmotr'),
    path('status/buy/<int:type>/',views.buy, name= 'buystatus'),
    path('kup_podpiska/', views.kup_podpiska, name='kup_podpiska'),
    path('otpiska/<int:type>/', views.otpiska, name='otpiska'),
    path('status/registr/',views.registr,name='registr'),
    path('search/', views.search_films, name='search_films'),






]
'''
login
reset_form
reset_done
reset_confirm
reset_complete
'''