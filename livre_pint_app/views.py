from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.messages import constants
from .utils import checar_senha
from .models import User


def homepage(request):
    return render(request, 'homepage.html')


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/homepage/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        foto_perfil = request.FILES.get("photo")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpassword = request.POST.get("confpassword")

    if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
        messages.add_message(
            request, constants.ERROR, 'Por favor, preencha todos os dados corretamente!')
        return render(request, 'cadastro.html')

    usuario = User.objects.filter(username=username)
    if usuario:
        messages.add_message(request, constants.WARNING,
                             'Ops! Já existe um usuário com este nome no sistema.')
        return redirect('/logar/')

    email = User.objects.filter(email=email)
    if email:
        messages.add_message(request, constants.WARNING,
                             'Ops! Já existe um usuário com este email no sistema.')
        return redirect('/logar/')

    senha_valida = checar_senha(request,
                                password=password, confirm_password=confpassword)
    if not senha_valida:
        return render(request, 'cadastro.html')

    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            foto_perfil=foto_perfil,
        )
        user.save()
        messages.add_message(request, constants.SUCCESS,
                             'Usuário cadastrado com sucesso!')
        return redirect('/logar/')
    except TypeError:
        messages.add_message(request, constants.ERROR,
                             f'{TypeError}')
        return redirect('/logar/')
    except:
        messages.add_message(request, constants.ERROR,
                             'Tivemos um erro interno no sistema')


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/homepage/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos!')
            return render(request, 'login.html')
        else:
            auth.login(request, user)
            return redirect('/homepage/')


def sair(request):
    auth.logout(request)
    return redirect('/logar')
