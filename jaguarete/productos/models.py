from django.db import models


class Categoria(models.Model):
    rubro = models.CharField(max_length=50, help_text='El rubro al que pertenece cada producto')
    descripcion = models.TextField(help_text='Descripcion de la seccion en la que se encuentra el producto')

    def __str__(self):
        return self.rubro


class Producto(models.Model):
    """Los datos principales de los productos a vender."""
    nombre = models.CharField(max_length=50, help_text='Nombre del producto')
    image = models.ImageField()
    descripcion = models.TextField(help_text='Descripción del producto')
    precio = models.FloatField()
    rubro = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()
    fecha_entrada = models.DateTimeField(auto_now_add=True, help_text='Fecha cuando introdujeron el producto')

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    """Datos de los clientes"""
    nombre = models.CharField(max_length=50, help_text='Nombre del cliente')
    apellido = models.CharField(max_length=50, help_text='Apellido del cliente')
    email = models.EmailField(max_length=100, help_text='e-mail del cliente')
    telefono = models.CharField(max_length=20, help_text='Número de contacto')

    def __str__(self):
        return self.apellido, self.nombre


class Canasta(models.Model):
    """Datos de los productos que están en la canasta"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.FloatField()
