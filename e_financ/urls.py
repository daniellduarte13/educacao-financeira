from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL para a página inicial
    path('conceitos-basicos/', views.conceitos_basicos, name='conceitos_basicos'),
    path('orcamento-pessoal/', views.orcamento_pessoal, name='orcamento_pessoal'),
    path('poupanca/', views.poupanca, name='poupanca'),
    path('psicologia-dinheiro/', views.psicologia_dinheiro, name='psicologia_dinheiro'),
    path('empreendedorismo-financas/', views.empreendedorismo_financas, name='empreendedorismo_financas'),  # Nova URL
    path('impostos-tributacao/', views.impostos_tributacao, name='impostos_tributacao'),
    path('credito-score/', views.credito_score, name='credito_score'),
    path('fundo-emergencia/', views.fundo_emergencia, name='fundo_emergencia'),
    path('custo-oportunidade/', views.custo_oportunidade, name='custo_oportunidade'),
    path('renda-gastos/', views.renda_gastos, name='renda_gastos'),
    path('investimentos/', views.investimentos, name='investimentos'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/delete/', views.delete_profile_view, name='delete_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('simulador-investimento/', views.simulador_investimento, name='simulador_investimento'),
    path('rede-social/', views.rede_social_view, name='rede_social'),  # Nova URL
    path('delete-publicacao/<int:publicacao_id>/', views.delete_publicacao, name='delete_publicacao'),
]
