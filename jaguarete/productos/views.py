from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, FormBuscar
from .models import *
from .utils import stock_avg


def inicio(request):
    return render(request, 'inicio.html')


def producto(request):
    return render(request, 'productos/productos.html')



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html',
                  {'productos': productos})  # Añadir diccionario contexto como tercer argumento.
    # La clave del contexto es la referencia en base.html,
    # El valor es la variable de la funcion.


def buscar_producto(request):
    buscar_text = request.GET.get('buscar', '')  # Si no hay un parametro a buscar por defecto arroja una cadena vacía.
    form = FormBuscar(request.GET)
    productos = set()
    if form.is_valid() and form.cleaned_data['buscar']:
        buscar = form.cleaned_data['buscar']
        buscar_en = form.cleaned_data.get('buscar_en') or 'producto'
        if buscar_en == 'producto':
            productos = Producto.objects.filter(nombre__icontains=buscar)

        else:
            categorias = Categoria.objects.filter(rubro__icontains=buscar)
            for categoria in categorias:
                for producto in categoria.rubro_set.all():
                    productos.add(producto)
    return render(request, 'productos/resultado_busqueda.html',
                  {'form': form, 'buscar_texto': buscar_text, 'productos': productos})


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} ha sido creado')
            return redirect('inicio')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'productos/registro.html', context)


def canasta(request):
    return render(request, 'productos/carro.html')


def login(request):
    return render(request, 'productos/login.html')


def nosotros(request):
    return render(request, 'productos/acerca_de.html')
