from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('numero_cuenta', 'nombre_cliente')
    search_fields = ('numero_cuenta',)

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('tipo_transaccion', 'monto', 'fecha_transaccion', 'cuenta')
    search_fields = ('tipo_transaccion',)