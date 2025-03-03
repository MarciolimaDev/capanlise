from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Sorteio, Premio, Dezena
from rest_framework import generics
from .serializers import SorteioSerializer
from django.db.models import Count
from django.db import models


# Create your views here.
def home(request):
    ano = request.GET.get('anoEdicao')
    sorteio_num = request.GET.get('sorteio')
    premio_ordem = request.GET.get('premio')

    #filtrando os resultados
    resultados = Premio.objects.all()

    if ano:
        resultados = resultados.filter(sorteio__ano=ano)
    if sorteio_num:
        resultados = resultados.filter(sorteio__numero=sorteio_num)
    if premio_ordem:
        resultados = resultados.filter(ordem=premio_ordem)

    # obtendo os anos disponíveis para o filtro
    anos_disponiveis = Sorteio.objects.values_list('anoEdicao', flat=True).distinct()

    context = {
        'resultados': resultados,
        'anos_disponiveis': anos_disponiveis,
        'ano_selecionado': ano,
        'sorteio_selecionado': sorteio_num,
        'premio_selecionado': premio_ordem,
    }
    return render(request, 'usuario/home.html', context)

class SorteioListView(generics.ListAPIView):
    queryset = Sorteio.objects.all().order_by('-anoEdicao', '-numeroEdicao') #ordem do mais recente ao mais antigo
    serializer_class = SorteioSerializer


def results(request):
    #edicao_selecionada = request.GET.get('edicao', None)
    sorteios = Sorteio.objects.all().order_by('-anoEdicao', '-numeroEdicao')  # Ordena do mais recente para o mais antigo
    return render(request, 'usuario/results.html')


from django.http import JsonResponse
from django.db.models import Count
from .models import Sorteio, Dezena

def analise_numeros(request):
    """ Retorna os 20 números mais sorteados dentro de um intervalo de edições """
    inicio = request.GET.get("inicio")  # Ex: "1/2016"
    fim = request.GET.get("fim")        # Ex: "4/2016"

    if not inicio or not fim:
        return JsonResponse({"error": "Os parâmetros 'inicio' e 'fim' são obrigatórios."}, status=400)

    try:
        # Convertendo os valores do filtro para inteiros
        inicio_num, inicio_ano = map(int, inicio.split('/'))
        fim_num, fim_ano = map(int, fim.split('/'))

        # Filtrando os sorteios dentro do intervalo exato
        sorteios = Sorteio.objects.filter(
            (models.Q(anoEdicao=inicio_ano, numeroEdicao__gte=inicio_num) | models.Q(anoEdicao__gt=inicio_ano)) &
            (models.Q(anoEdicao=fim_ano, numeroEdicao__lte=fim_num) | models.Q(anoEdicao__lt=fim_ano))
        )

        if not sorteios.exists():
            return JsonResponse({"error": "Nenhum sorteio encontrado para esse intervalo."}, status=404)

        # Pegando apenas as dezenas dos sorteios filtrados
        dezenas = Dezena.objects.filter(premio__sorteio__in=sorteios)

        # Contando quantas vezes cada número apareceu dentro do intervalo correto
        contagem = (
            dezenas.values("numero")
            .annotate(frequencia=Count("numero"))
            .order_by("-frequencia")[:20]
        )

        return JsonResponse({"top_20_numeros": list(contagem)})

    except ValueError:
        return JsonResponse({"error": "Formato de data inválido. Use o formato correto: 'numeroEdicao/ano'."}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

def analise_view(request):
    return render(request, 'usuario/analyze.html')