# 🎯 AcreCap Legal Analyzer

AcreCap Legal Analyzer é um sistema desenvolvido em **Django** para analisar o histórico de resultados do **AcreCap Legal**. Com base nos filtros aplicados, o sistema exibe as dezenas mais sorteadas dentro do intervalo selecionado.

## 🚀 Funcionalidades

- 📊 **Análise Estatística**: Mostra as dezenas mais sorteadas com base nos filtros definidos.
- 🔍 **Filtragem Avançada**: Permite selecionar intervalos de sorteios para análise personalizada.
- 📁 **Armazenamento de Dados**: Registra os resultados de edições anteriores para consultas futuras.
- 🌐 **API em Django**: Disponibiliza endpoints para consulta dos dados.
- 📈 **Visualização Interativa**: Apresenta gráficos e tabelas dinâmicas para análise intuitiva.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django + Django REST Framework
- **Frontend**: JavaScript (para exibição dos dados)
- **Banco de Dados**: SQLite/PostgreSQL (dependendo da necessidade)

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/MarciolimaDev/evenx.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd evenx
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor Django:
   ```bash
   python manage.py runserver
   ```

## 🔗 Endpoints da API

| Método  | Endpoint       | Descrição |
|---------|---------------|-----------|
| GET     | `/api/resultados/` | Lista todos os resultados armazenados. |
| GET     | `/api/analise/?inicio=XX&fim=YY` | Retorna as dezenas mais sorteadas entre os sorteios `XX` e `YY`. |

## 🏗️ Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** e **pull requests**. 🚀

## 📜 Licença

Este projeto é licenciado sob a **MIT License** - veja o arquivo `LICENSE` para mais detalhes.

---

💡 *Desenvolvido por Márcio Lima*