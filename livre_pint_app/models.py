import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser, UserManager):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=264)
    password = models.CharField(max_length=264)
    foto_perfil = models.ImageField(
<<<<<<< HEAD
        upload_to='foto_perfil', blank=True, null=True)

    def __str__(self):
        return self.username
=======
        upload_to='foto_usuarios', blank=True, null=True)

    def __str__(self):
        return self.username

    # @mark_safe
    # def icone(self) -> str:
    #     return f'<img width="30px" src="/media/{self.foto_perfil}">'


# class Imagem(models.Model):
#     photos = models.ImageField(upload_to='fotos_postagens_users')


# class Post(models.Model):
#     titulo = models.CharField(max_length=200)
#     imagem = models.ManyToManyField(
#         Imagem, related_name='fotos_posts', blank=True)
#     data_post = models.DateTimeField(auto_now=True)
#     usuario = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='postagem_user')

#     def __str__(self):
#         return self.titulo
>>>>>>> 7e11aa10d035a3e8e63423f146927e8081360b30
