<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from django.contrib import messages
from django.contrib.messages import constants


def post(request):
    posts = Post.objects.all()
    if request.method == "GET":
        return render(request, 'post.html', {'posts': posts})
    elif request.method == "POST":
        titulo = request.POST.get("titulo")
        imagem = request.FILES.get("imagem")
        usuario = request.user

        post = Post(
            titulo=titulo,
            imagem=imagem,
            usuario=usuario,
        )
        post.save()
        messages.add_message(request, constants.SUCCESS,
                             'Post realizado com sucesso!')
        return redirect('/homepage')


def perfil(request):
    posts = Post.objects.filter(usuario_id=request.user.id)
    if request.method == "GET":
        return render(request, 'perfil.html', {'posts': posts})
    elif request.method == "POST":
        titulo = request.POST.get("titulo")
        imagem = request.FILES.get("imagem")
        usuario = request.user

        post = Post(
            titulo=titulo,
            imagem=imagem,
            usuario=usuario,
        )
        post.save()
        messages.add_message(request, constants.SUCCESS,
                             'Post realizado com sucesso!')
        return redirect('/homepage')
=======
from django.shortcuts import render


def post(request):
    return render(request, 'post.html')
>>>>>>> 7e11aa10d035a3e8e63423f146927e8081360b30
