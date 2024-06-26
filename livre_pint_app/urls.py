from django.urls import path
from .import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('perfil/', views.perfil, name='perfil'),
    path('sair/', views.sair, name='sair'),
]
