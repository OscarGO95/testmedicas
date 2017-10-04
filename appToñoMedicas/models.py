from django.db import models

class Cliente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    celular = models.CharField(max_length=12, blank=True)
    fijo = models.CharField(max_length=10, blank=True)

class Producto(models.Model):
    precio = models.DecimalField(max_digits=20, decimal_places=5)

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valor = models.DecimalField(max_digits=50, decimal_places=15)
    fecha = models.DateTimeField(auto_now=False,auto_now_add=True)

class Direcciones(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)

class Drogueria(models.Model):
    nombre = models.CharField(max_length=30)

class Calificaciones(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    drogueria = models.ForeignKey(Drogueria, on_delete=models.CASCADE)
    estrellas = models.SmallIntegerField()
    comentario = models.CharField(max_length=150)

