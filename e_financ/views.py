from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import LoginForm, RegisterForm, PublicacaoForm
from .models import Publicacao

def index(request):
    return render(request, 'index.html')  # Renderiza o template index.html

def conceitos_basicos(request):
    return render(request, 'conceitos_basicos.html')  # Renderiza o template conceitos_basicos.html

def orcamento_pessoal(request):
    return render(request, 'orcamento_pessoal.html')  # Renderiza o template orcamento_pessoal.html

def poupanca(request):
    return render(request, 'poupanca.html')  # Renderiza o template poupanca.html

def psicologia_dinheiro(request):
    return render(request, 'psicologia_dinheiro.html')  # Renderiza o template psicologia_dinheiro.html

def empreendedorismo_financas(request):
    return render(request, 'empreendedorismo_financas.html')  # Renderiza o template empreendedorismo_financas.html

def impostos_tributacao(request):
    return render(request, 'impostos_tributacao.html')  # Renderiza o template impostos_tributacao.html

def credito_score(request):
    return render(request, 'credito_score.html')  # Renderiza o template credito_score.html

def fundo_emergencia(request):
    return render(request, 'fundo_emergencia.html')  # Renderiza o template fundo_emergencia.html

def custo_oportunidade(request):
    return render(request, 'custo_oportunidade.html')  # Renderiza o template custo_oportunidade.html

def renda_gastos(request):
    return render(request, 'renda_gastos.html')  # Renderiza o template renda_gastos.html

def investimentos(request):
    return render(request, 'investimentos.html')  # Renderiza o template investimentos.html

@login_required
def simulador_investimento(request):
    return render(request, 'simulador_investimento.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redireciona para a página inicial após o login
            else:
                form.add_error(None, 'Nome de usuário ou senha incorretos.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')  # Redireciona para a página inicial após o registro
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    publicacoes = Publicacao.objects.filter(usuario=request.user).order_by('-data_publicacao')
    return render(request, 'profile.html', {'user': request.user, 'publicacoes': publicacoes})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RegisterForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile_view(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.user.username)
        user.delete()
        auth_logout(request)
        return redirect('index')
    return render(request, 'delete_profile.html')

def logout_view(request):
    auth_logout(request)
    return redirect('index')

@login_required
def rede_social_view(request):
    if request.method == 'POST':
        form = PublicacaoForm(request.POST)
        if form.is_valid():
            publicacao = form.save(commit=False)
            publicacao.usuario = request.user
            publicacao.save()
            messages.success(request, 'Publicação enviada com sucesso!')
            return redirect('rede_social')
        else:
            messages.error(request, 'Erro ao enviar a publicação. Verifique os dados e tente novamente.')
    else:
        form = PublicacaoForm()

    # Buscar todas as publicações
    publicacoes = Publicacao.objects.all().order_by('-data_publicacao')

    return render(request, 'rede_social.html', {'form': form, 'publicacoes': publicacoes})

@login_required
def delete_publicacao(request, publicacao_id):
    publicacao = get_object_or_404(Publicacao, id=publicacao_id, usuario=request.user)
    if request.method == 'POST':
        publicacao.delete()
        messages.success(request, 'Publicação excluída com sucesso!')
        return redirect('profile')
    return render(request, 'confirm_delete.html', {'publicacao': publicacao})
