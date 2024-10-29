from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Categoria(models.Model):
    name=models.CharField(max_length=100,verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.name

class Producto (models.Model):
    name=models.CharField(max_length=100,verbose_name="Nombre")
    detail=models.TextField(verbose_name="Detalle")
    published=models.DateTimeField(default=now,verbose_name="Fecha de publicacion")
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Autor")##cascada ya que elimina todo lo que tenga estaclave foranea
    category=models.ManyToManyField(Categoria,verbose_name="Categorias") ##crea la tabla intermedia de muchos a muchos
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    image=models.ImageField(upload_to="productos",null=True,blank=True,verbose_name="Imagen")
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.name
