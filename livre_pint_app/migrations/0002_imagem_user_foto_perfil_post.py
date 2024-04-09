# Generated by Django 5.0.4 on 2024-04-09 17:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livre_pint_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='fotos_postagens_users')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='foto_perfil',
            field=models.ImageField(default='foto_perfil.png', upload_to='foto_perfil'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data_post', models.DateTimeField(auto_now=True)),
                ('imagem', models.ManyToManyField(blank=True, related_name='fotos_posts', to='livre_pint_app.imagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagem_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]