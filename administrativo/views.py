from django.shortcuts import render, redirect, get_object_or_404
from .forms import DezenaForm, SorteioForm
from usuario.models import Sorteio, Premio, Dezena
# Create your views here.

def dashboard(request):
    return render(request, 'administrativo/dashboard.html')


def listar_sorteios(request):
    sorteios = Sorteio.objects.all().order_by("-dataEdicao") #Ordenando do mais recente
    return render(request, "administrativo/listar_sorteios.html", {"sorteios": sorteios})

def listar_premios(request, sorteio_id):
    sorteio = get_object_or_404(Sorteio, id=sorteio_id)
    premios = sorteio.premios.all().order_by("ordemPremio") # Ordenando pelo Prêmio
    return render(request, "administrativo/listar_premios.html", {"sorteio": sorteio, "premios": premios})

def adicionar_dezenas(request, sorteio_id, premio_id):
    premio = get_object_or_404(Premio, id=premio_id, sorteio_id=sorteio_id)

    if request.method == "POST":
        form = DezenaForm(request.POST)
        if form.is_valid():
            dezenas_str = form.cleaned_data['dezenas']
            dezenas_list = [int(num.strip()) for num in dezenas_str.split(',') if num.strip().isdigit()] 

            # Criar objetos Dezenas vinculadas ao prêmio
            for numero in dezenas_list:
                Dezena.objects.create(premio=premio, numero=numero)

    
            return redirect('administracao:listar_premios', sorteio_id=sorteio_id) #redirecionar após adicionar
    else:
        form = DezenaForm()

    return render(request, 'administrativo/adicionar_dezenas.html', {'form': form, 'premio': premio})



def criar_sorteio(request):
    if request.method == 'POST':
        form = SorteioForm(request.POST)
        if form.is_valid():
            sorteio = form.save(commit=False) # Salva sem enviar ao banco ainda
            quantidade_premios = form.cleaned_data['quantidade_premios']
            sorteio.save() # Agora salva no banco

            # Criar automaticamente os prêmios para esse sorteio
            for i in range(1, quantidade_premios +1):
                Premio.objects.create(sorteio=sorteio, ordemPremio=i)

            return redirect('administracao:listar_sorteios') #Redireciona para lista de Sorteios

    else:
        form = SorteioForm()

    return render(request, 'administrativo/criar_sorteio.html', {'form': form})