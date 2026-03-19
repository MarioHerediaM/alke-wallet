from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.nombre
    
class Cuenta(models.Model):
    numero_cuenta = models.CharField(max_length=100, unique=True)
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_cuenta
    
class Transaccion(models.Model):
    tipo_transaccion = models.CharField(max_length=100)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo_transaccion} - {self.fecha_transaccion}'