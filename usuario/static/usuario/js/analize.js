document.addEventListener("DOMContentLoaded", function () {
    carregarEdicoes();
});

async function carregarEdicoes() {
    const response = await fetch('/api/sorteios/');
    const data = await response.json();

    const inicioSelect = document.getElementById('inicio');
    const fimSelect = document.getElementById('fim');

    data.forEach(sorteio => {
        const option = document.createElement('option');
        option.value = `${sorteio.numeroEdicao}/${sorteio.anoEdicao}`;
        option.textContent = `${sorteio.numeroEdicao}ª Edição (${sorteio.dataEdicao})`;
        
        inicioSelect.appendChild(option.cloneNode(true));
        fimSelect.appendChild(option);
    });

    // Definir valores padrão (primeira e última edição)
    inicioSelect.selectedIndex = 0;
    fimSelect.selectedIndex = fimSelect.options.length - 1;
}

async function buscarAnalise() {
    const inicio = document.getElementById('inicio').value;
    const fim = document.getElementById('fim').value;

    const response = await fetch(`/api/analise/?inicio=${inicio}&fim=${fim}`);
    const data = await response.json();

    const resultadosDiv = document.getElementById('resultados');
    resultadosDiv.innerHTML = "";

    data.top_20_numeros.forEach(item => {
        const span = document.createElement('span');
        span.classList.add('dezena');
        //span.textContent = `${item.numero} (${item.frequencia})`;
        span.textContent = `${item.numero}`

        if (item.frequencia >= 10) {
            span.classList.add('quente');
        } else if (item.frequencia >= 5) {
            span.classList.add('morno');
        } else {
            span.classList.add('fraco');
        }

        resultadosDiv.appendChild(span);
    });
}
