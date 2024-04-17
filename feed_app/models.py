from django.db import models
from livre_pint_app.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos_posts', blank=True, null=True)
    data_post = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='postagem_user')

    def __str__(self) -> str:
        return self.usuario.username
