import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser, UserManager):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=264)
    password = models.CharField(max_length=264)
    foto_perfil = models.ImageField(
        upload_to='foto_perfil', blank=True, null=True)

    def __str__(self):
        return self.username


# class Post(models.Model):
#     titulo = models.CharField(max_length=200)
#     imagem = models.ImageField(upload_to='fotos_posts', blank=True, null=True)
#     data_post = models.DateTimeField(auto_now=True)
#     usuario = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='postagem_user')

#     def __str__(self):
#         return self.titulo
