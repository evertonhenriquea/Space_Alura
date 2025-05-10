from django.shortcuts import render


def index(request):

    dados = {
    1: {"nome": "Nebulosa De Carina",
        "legenda": " A nebulosa se encontra a uma distância estimada entre 6.500 e 10.000 anos-luz da Terra. Ele aparece na direção da constelação de Carina e situa-se no braço de Carina-Sagitário."},
    2: {"nome": "Earthrise",
        "legenda": "A Terra, ao fundo, é visível como um globo azul e branco, com nuvens e massas de terra claramente definidas."}
}
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')