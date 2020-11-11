from django.db import models

# Create your models here.

class Compañia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    Compañia = models.ForeignKey(Compañia, on_delete = models.PROTECT)
    fecha_lanzamiento = models.DateField()
    imagen = models.ImageField(upload_to="Juego",null=True)
    


    def __str__(self):
        return self.nombre


opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Problemas"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()


def __str__(self):
    return self.nombre



