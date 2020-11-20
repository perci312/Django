from django.urls import path
from .views import index
from .views import Contacto
from .views import login
from .views import registro
from .views import Tienda
from .views import agregar_juego,listar_juegos,modificar_juego,eliminar_juego
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/', index,name='index'),
    path('', index,name='index'),
    path('Contacto/',Contacto,name='Contacto'),
    path('login/', login,name='login'),
    path('registro/', registro,name='registro'),
    path('Tienda/', Tienda,name='Tienda'),
    path('agregar_juego/',agregar_juego,name="agregar_juego"),
    path('listar_juegos/',listar_juegos,name="listar_juegos"),
    path('modificar_juego/<id>/',modificar_juego,name="modificar_juego"),
    path('eliminar_juego/<id>/',eliminar_juego,name="eliminar_juego"),
    
    

]