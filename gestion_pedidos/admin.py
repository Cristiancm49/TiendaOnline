
from django.contrib import admin
from gestion_pedidos.models import Cliente, Articulos, Pedido

# Register your models here.

class Clientes_Admin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre", "telefono")

class Articulos_admin(admin.ModelAdmin):
    list_filter =("seccion",) 

class Pedidos_admin(admin.ModelAdmin):
    list_display= ("numbero_pedido", "fecha")
    list_filter= ("fecha",)
    date_hierarchy= "fecha"

admin.site.register(Cliente, Clientes_Admin)
admin.site.register(Articulos, Articulos_admin)
admin.site.register(Pedido, Pedidos_admin)