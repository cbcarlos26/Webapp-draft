from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['contrasena']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio.html')
        else:
            messages.success(request, 'Hubo un error, intenta nuevamente')
            return redirect('login.html')

    return render(request, 'login.html')