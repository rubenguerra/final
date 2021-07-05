from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/', views.producto, name='producto'),
    path('canasta/', views.canasta, name='canasta'),
    path('lista/', views.lista_productos, name='lista_productos'),
    path('buscar_producto/', views.buscar_producto, name='buscar'),
    path('registro/', views.registro, name='registro'),
    #path('login/', views.login, name='login'),
    path('nosotros/', views.nosotros, name='nosotros')
    # path('ruta/', login_required(vista-proteger), name='vista-a-proteger')
]
