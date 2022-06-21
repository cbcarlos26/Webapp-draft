from django.db import models
# Create your models here.

#This class is created to be an uneditable option, just the admin will be able to edit or delet it
class Origen(models.Model):
    municipio = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.municipio}, {self.departamento}'
#This class is created to catch the user information and send it to the database
class Vehiculo(models.Model):
    fecha_in = models.DateField(auto_now=True)
    placa = models.CharField('Placa de vehiculo', max_length=10)
    marca = models.CharField('Marca de vehiculo', max_length=20)
    modelo = models.CharField('Modelo de vehiculo', max_length=20)
    color = models.CharField('Color de vehiculo', max_length=15)
    imagen = models.ImageField(upload_to='photos/photos')
    cedula_p = models.CharField('Cedula de propietario', max_length=15)
    nombre_p = models.CharField('Nombre de propietario', max_length=25)
    apellido_p = models.CharField('Apellido de propietario', max_length=25)
    contacto_p = models.CharField('Contacto propietario', max_length=15)
    origen = models.ForeignKey(Origen, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Carro {self.placa}: Propietario {self.nombre_p} {self.apellido_p}, ' \
               f'Fecha de ingreso: {self.fecha_in}'