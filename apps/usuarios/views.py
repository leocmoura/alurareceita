import email
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    """Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'Campo nome não pode ficar em branco!')
            # print('O campo nome não pode ficar em branco!')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'Campo email não pode ficar em branco!')
            # print('O campo email não pode ficar em branco!')
            return redirect('cadastro')

        if senhas_diferentes(senha, senha2):
            messages.error(request, 'Senhas diferentes')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        # print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """Realiza login de usuario no sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    """Realiza logout do usuario do sistema"""
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """Renderiza o dashboard do usuario logado ou o index se não estiver logado"""
    if request.user.is_authenticated:
        # id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=request.user.id)

        dados = {
            'receitas' : receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def senhas_diferentes(senha, senha2):
    return senha != senha2
