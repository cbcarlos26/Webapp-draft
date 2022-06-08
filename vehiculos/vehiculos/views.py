from django.shortcuts import render, get_object_or_404, redirect
from vehiculos.models import Vehiculo
from webapp.forms import VehiculoForm
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.
#This function return the "vehiculos registrados" webpage, it gets a count and all objects from the database
def registro_vehiculos(request):
    no_vehiculos = Vehiculo.objects.count()
    vehiculos = Vehiculo.objects.all()
    return render(request, 'registro_vehiculos.html', {'no_vehiculos': no_vehiculos, 'vehiculos':vehiculos})
#This function return the "Detalles de vehiculo" webpage, it gets every field of each object
def ver_detalle(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo})
#This function allow to edit the fields of an especific object
def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    if request.method == 'POST':
        formaVehiculo = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if formaVehiculo.is_valid():
            formaVehiculo.save()
            return redirect('registro')
    else:
        formaVehiculo = VehiculoForm(instance=vehiculo)

    return render(request, 'editar_vehiculo.html', {'formaVehiculo':formaVehiculo})