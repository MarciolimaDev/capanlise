document.addEventListener("DOMContentLoaded", function () {
    const selectEdicao = document.getElementById("edicao");
    const resultadosDiv = document.getElementById("resultados");
    const freqDezenasDiv = document.getElementById("frequencia-dezenas");

    let sorteiosData = []; // Variável para armazenar os dados da API

    // Função para carregar os sorteios da API
    function carregarSorteios() {
        fetch('/api/sorteios/')
            .then(response => response.json())
            .then(data => {
                sorteiosData = data; // Salva os dados para uso posterior

                // Adiciona as edições no select
                selectEdicao.innerHTML = "";
                data.forEach((sorteio, index) => {
                    let option = document.createElement("option");
                    option.value = sorteio.id;
                    option.textContent = `${sorteio.numeroEdicao}ª Edição (${sorteio.dataEdicao})`;

                    // Seleciona a última edição por padrão
                    if (index === 0) option.selected = true;

                    selectEdicao.appendChild(option);
                });

                // Exibe os resultados da edição mais recente
                exibirResultados(data[0].id);
            })
            .catch(error => console.error("Erro ao carregar sorteios:", error));
    }

    // Função para exibir os resultados da edição selecionada
    function exibirResultados(edicaoId) {
        const sorteio = sorteiosData.find(s => s.id == edicaoId);
        if (!sorteio) return;

        resultadosDiv.innerHTML = `
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">${sorteio.numeroEdicao}ª Edição (${sorteio.dataEdicao})</h5>
                    ${sorteio.premios.map(premio => `
                        <p><strong>${premio.ordemPremio}º Prêmio:</strong></p>
                        <div class="dezenas-container">
                            ${premio.dezenas.map(dezena => `<span class="dezena">${dezena.numero}</span>`).join("")}
                        </div>
                    `).join("")}
                </div>
            </div>
        `;
    }

    // Atualiza os resultados quando o usuário muda a edição no filtro
    selectEdicao.addEventListener("change", function () {
        exibirResultados(this.value);
    });

    // Carrega os sorteios ao carregar a página
    carregarSorteios();
});