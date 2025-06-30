from django.shortcuts import render, redirect
from apps.usuarios.forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:   
            auth.login(request, usuario)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect('login')
        
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "As senhas não coincidem.")
                return redirect('cadastro')
            
            name= form["nome_cadastro"].value()
            email = form['email'].value()
            password = form['senha_1'].value()
            
            if User.objects.filter(username=name).exists():
                messages.error(request, "Nome de usuário já existe.")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=name,
                email=email, 
                password=password
            )
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('login')
