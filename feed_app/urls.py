from django.urls import path
from .import views


urlpatterns = [
    path('post/', views.post, name='post'),
    path('perfil/', views.perfil, name='perfil'),
]
