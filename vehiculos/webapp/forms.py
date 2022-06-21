from django.forms import ModelForm
from django import forms
from vehiculos.models import Vehiculo

#The form we will use is created here with a class and it inherit of the ModelForm class
class VehiculoForm(ModelForm):
    #The meta class is created and it will contain the model's class arguments
    class Meta:
        #The model class will be "Vehiculo" which is imported from "vehiculos.models"
        model = Vehiculo
        #The fields are added from the class model, it could be "__all__"
        fields = ('placa', 'marca', 'modelo', 'color', 'cedula_p', 'nombre_p', 'apellido_p',
                  'contacto_p', 'imagen', 'origen')
        #Here the fields' names can be added to be showed in the form but a placeholder is used
        labels = {
            'placa': '',
            'marca': '',
            'modelo': '',
            'color': '',
            'cedula_p': '',
            'nombre_p': '',
            'apellido_p': '',
            'contacto_p': '',
            'imagen': '',
            'origen':''
        }
        #The widgets ared added with html attributes
        widgets = {
            'placa': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                            'placeholder':'Placa del vehiculo'}),
            'marca': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                            'placeholder':'Marca del vehiculo'}),
            'modelo': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                             'placeholder':'Modelo del vehiculo'}),
            'color': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                            'placeholder':'Color del vehiculo'}),
            'cedula_p': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                               'placeholder':'Cedula de propietario'}),
            'nombre_p': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                               'placeholder':'Nombre de propietario'}),
            'apellido_p': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                                 'placeholder':'Apellido de propietario'}),
            'contacto_p': forms.TextInput(attrs={'class':'form-control', 'size':'100',
                                                 'placeholder':'Numero de contacto de propietario'}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control', 'align':'center'}),
            'origen':forms.Select(attrs={'class':'form-control'})}