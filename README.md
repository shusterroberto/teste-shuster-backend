Projeto de API de Filmes
Este projeto é uma API de backend em Python, criada com FastAPI, que permite consultar filmes e visualizar o histórico de pesquisas. A aplicação usa a API pública The One API para obter informações sobre filmes.

Pré-requisitos
Python 3.12 ou superior
Conta na The One API para obter uma chave de API
Configuração do Ambiente
Clone este repositório:

bash
Copiar código
git clone https://github.com/usuario/projeto-filmes.git
cd projeto-filmes
Crie um ambiente virtual (recomendado):

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

No Windows:
bash
Copiar código
.\venv\Scripts\activate
No Linux/Mac:
bash
Copiar código
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configuração da Chave da API:

Crie um arquivo .env na raiz do projeto e adicione a sua chave da API do The One API.
Exemplo do arquivo .env:
plaintext
Copiar código
API_KEY=your_api_key_here
Executando o Servidor
Inicie o servidor FastAPI com Uvicorn:

bash
Copiar código
uvicorn main:app --reload
Acesse a documentação interativa da API (Swagger) em http://127.0.0.1:8000/docs.

Endpoints da API
1. Consultar Filmes
Endpoint: /movies
Método: GET
Parâmetro opcional: title (string) - Filtra os filmes pelo título.
Exemplo:
http
Copiar código
GET http://127.0.0.1:8000/movies?title=The%20Hobbit
2. Consultar Histórico de Pesquisas
Endpoint: /history
Método: GET
Descrição: Retorna o histórico de pesquisas anteriores.
Exemplo:
http
Copiar código
GET http://127.0.0.1:8000/history
Executando Testes Unitários
Os testes unitários foram criados usando pytest. Para executar os testes:

Certifique-se de que está no diretório raiz do projeto.
Execute o comando:
bash
Copiar código
python -m pytest backend/tests
Os testes verificam a funcionalidade dos endpoints /movies e /history, bem como o registro de pesquisas no banco de dados.