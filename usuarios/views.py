from django.shortcuts import render
from .forms import *

def login(request):
    form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def logout(request):
    return render(request, 'usuarios/logout.html')
