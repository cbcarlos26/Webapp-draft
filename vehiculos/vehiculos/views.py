from django.shortcuts import render, get_object_or_404, redirect
from vehiculos.models import Vehiculo
from webapp.forms import VehiculoForm
from django.core.paginator import Paginator

# Create your views here.
#This function return the "vehiculos registrados" webpage, it gets a count and all objects from the database
def registro_vehiculos(request):
    no_vehiculos = Vehiculo.objects.count()
    lista_vehiculos = Vehiculo.objects.all().order_by('-fecha_in')
    p = Paginator(lista_vehiculos, 15)
    page = request.GET.get('page')
    vehiculos = p.get_page(page)
    nums = 'a' * vehiculos.paginator.num_pages
    return render(request, 'registro_vehiculos.html', {'no_vehiculos': no_vehiculos,
                                                       'vehiculos':vehiculos, 'nums':nums})

def vehiculos_buscados(request):
    if request.method == 'POST':
        buscado = request.POST['buscado']
        vehiculos_b = Vehiculo.objects.filter(placa__contains=buscado).order_by('-fecha_in')
        no_vehiculos = vehiculos_b.count()
        return render(request, 'vehiculos_buscados.html', {'buscado':buscado, 'vehiculos_b':vehiculos_b,
                                                           'no_vehiculos': no_vehiculos})

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
            return redirect('registro'), VehiculoForm()
    else:
        formaVehiculo = VehiculoForm(instance=vehiculo)
    return render(request, 'editar_vehiculo.html', {'formaVehiculo':formaVehiculo})