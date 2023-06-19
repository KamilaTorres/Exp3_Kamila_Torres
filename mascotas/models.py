from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class UsuarioPersonalizado(AbstractUser):
    es_administrador = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        "auth.Group", related_name="usuarios_personalizados", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="usuarios_personalizados", blank=True
    )
