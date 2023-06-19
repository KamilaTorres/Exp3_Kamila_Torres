from django.shortcuts import render,redirect
from .forms import RegistroUserForm,ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .decorators import solo_administrador_required
from .decorators import vista_restringida

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

@login_required
def gatos(request):
    return render(request,'gatos.html')

@login_required
def tarjetas(request):
    return render(request,'tarjetas.html')

@login_required
def Formulario(request):
    return render(request,'Formulario.html')

@login_required
def Vision(request):
    return render(request,'Vision.html')


def Login(request):
    return render(request,'Login.html')

def registrar(request):
     data={
          'form' : RegistroUserForm()
     }
     if request.method=="POST":
          formulario = RegistroUserForm(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user=authenticate(username=formulario.cleaned_data["username"],
                                 password=formulario.cleaned_data["password1"])
               login(request, user)
               return redirect('inicio')
          data["form"]=formulario
     return render(request, 'registration/registrar.html',data)

@solo_administrador_required
def mostrar(request):
     mascotitas = Producto.objects.all()
     datos={'mascotitas':mascotitas}
     return render(request, 'mostrar.html', datos)

from django.shortcuts import render, redirect, get_object_or_404

@solo_administrador_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            if Producto.objects.filter(nombre=nombre).exists():
                form.add_error('nombre', 'Ya existe un producto con este nombre')
            else:
                form.save()
                return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@solo_administrador_required
def eliminar_producto(request, nombre):
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

@solo_administrador_required
def modificar_producto(request, nombre):
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'modificar_producto.html', {'form': form, 'producto': producto})

@solo_administrador_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})


