from django.urls import path, include
from apps.usuarios.views import *

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]
