from django.urls import path
from . import views


app_name = 'administracao'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('sorteios/', views.listar_sorteios, name='listar_sorteios'),
    path('sorteios/<int:sorteio_id>/premios/', views.listar_premios, name='listar_premios'),
    path('sorteios/criar/', views.criar_sorteio, name='criar_sorteio'),
    path('sorteios/<int:sorteio_id>/premios/<int:premio_id>/adicionar-dezenas/', views.adicionar_dezenas, name='adicionar_dezenas'),
]