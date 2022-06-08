#Import the tools we will use to respond or redirect to requests
from django.shortcuts import render, redirect
# Create your views here.
#Import the form we will use to apply in our webapp
from webapp.forms import VehiculoForm
#Create a function and add the form with the data validation and save it in the connected data base
def inicio(request):
    #If the form is valid just save it
    if request.method == 'POST':
        formaVehiculo = VehiculoForm(request.POST, request.FILES)
        if formaVehiculo.is_valid():
            formaVehiculo.save()
            #When the information is saved, the action will redirect to the webpage "registro"
            return redirect('registro')
    #If not the form will continue empty
    else:
        formaVehiculo = VehiculoForm()
    #Return the principal webpage of the webapp which is located in the folder templates
    return render(request, 'index.html', {'formaVehiculo':formaVehiculo})