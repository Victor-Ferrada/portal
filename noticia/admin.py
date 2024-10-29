from django.contrib import admin
from .models import Categoria, Producto

# crearemos una clase para personalizar el panel de administracion para que rebnderice los campos de la tabla de productos a la fuerza
#un chanchullo para que se vea mejor
#solo para el created y updated
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria,CategoriaAdmin) ##aca genera la instancia de un objeto creando otro objeto de la clase CategoriaAdmin
admin.site.register(Producto,ProductoAdmin)