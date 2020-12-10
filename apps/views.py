from django.shortcuts import render,redirect,get_object_or_404
from .models import Juego
from .forms import ContactoForm,JuegoForm,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required , permission_required
from rest_framework import viewsets
from .serializers import JuegoSerializer

# Create your views here.

class JuegoViewset(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

    def get_queryset(self):
        juegos = Juego.objects.all()

        nombre = self.request.GET.get('nombre')
        if nombre:
            juegos = juegos.filter(nombre__contains=nombre)

        return juegos


def index(request):
    return render(request, 'apps/index.html')

@login_required(login_url='/account/login/')
def Contacto(request):
    data = {
        'form':ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto enviado"
        else:
            data["form"] = formulario    

    return render(request, 'apps/Contacto.html',data)



def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to='index')
        data['form'] = formulario

    return render(request, 'registration/registro.html',data)

def Tienda(request):
    juegos = Juego.objects.all()
    data ={
        'juegos': juegos
    }
    return render(request, 'apps/Tienda.html',data)

@permission_required('apps.add_juego')
def agregar_juego(request):
    data = {
        'form':JuegoForm()
    }
    if request.method == 'POST':
        formulario = JuegoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Registrado")
        else:
            data["form"] = formulario

    return render(request, 'apps/agregar.html',data)

@permission_required('apps.view_producto')
def listar_juegos(request):
    juegos = Juego.objects.all()

    data = {
        'juegos':juegos
    }
    return render(request, 'apps/listar.html',data)

@permission_required('apps.change_juego')
def modificar_juego(request,id):


    juego = get_object_or_404(Juego,id=id)
    data={
        'form':JuegoForm(instance=juego)
    }

    if request.method == 'POST':
        formulario = JuegoForm(data=request.POST, instance=juego, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"modificado correctamente")
            return redirect(to=listar_juegos)
            data["form"] = formulario

    return render(request,'apps/modificar.html',data)

@permission_required('apps.delete_juego')
def eliminar_juego(request,id):
    juego = get_object_or_404(Juego,id=id)
    juego.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar_juegos")




