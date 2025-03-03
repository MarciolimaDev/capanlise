from django.urls import path
from . import views
from .views import SorteioListView, analise_numeros

urlpatterns = [
    path('', views.home, name='home'),
    path('resultados/', views.results, name='results'),
    path('api/sorteios/', SorteioListView.as_view(), name='sorteio-list'),
    path('api/analise/', analise_numeros, name="analise_numeros"),
    path('analize/', views.analise_view, name='analize'),
]