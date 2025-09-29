from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar a galeria.")
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404 (Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para buscar fotografias.")
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render (request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar a galeria.")
        return redirect('login')
    
    form = FotografiaForm
    if request.method == "POST":
        form = FotografiaForm(request.POST)
        if form.is_valid():
            form.save
            messages.success(request, "Imagem cadastrada com sucesso!")
            return redirect('index')
        
    return render(request, 'galeria/nova_imagem.html', {"form": form})

def editar_imagem(request):
    pass

def deletar_imagem(request, foto_id):
    pass