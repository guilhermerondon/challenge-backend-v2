# Pokedex API (Challenge Backend)

Este projeto implementa uma API REST para gerenciamento de Treinadores, Pokémons, relacionamento entre eles e uma funcionalidade adicional de batalha entre Pokémons.
Des envolvido com Django e Django REST Framework.

1. Tecnologias Utilizadas

Python 3.12+

Django 5

Django REST Framework

Requests (para integração com a PokeAPI)

2. Como Executar o Projeto
2.1. Clonar o repositório
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio

2.2. Criar ambiente virtual (opcional, recomendado)
python -m venv venv
venv\Scripts\activate  # Windows

2.3. Instalar dependências
pip install -r requirements.txt

2.4. Aplicar migrações
python manage.py migrate

2.5. Executar servidor
python manage.py runserver


A API ficará disponível em:

http://127.0.0.1:8000/

3. Endpoints da API

Abaixo estão todos os endpoints organizados por recurso.

3.1. Treinadores
Listar todos / Criar novo
GET  /api/trainers/
POST /api/trainers/


Exemplo de criação:

{
  "name": "Ash Ketchum",
  "age": 10
}

Detalhar, atualizar ou remover
GET    /api/trainers/<id>/
PUT    /api/trainers/<id>/
DELETE /api/trainers/<id>/

3.2. Pokémons
Listar todos / Criar novo
GET  /api/pokemons/
POST /api/pokemons/


Exemplo JSON:

{
  "name": "pikachu",
  "photo": "https://url_da_imagem.png",
  "height": 4,
  "weight": 60
}

Detalhar, atualizar ou remover
GET    /api/pokemons/<id>/
PUT    /api/pokemons/<id>/
DELETE /api/pokemons/<id>/

3.3. Relacionar Pokémon com Treinador
Adicionar Pokémon ao treinador
POST /api/trainer-pokemons/


Body:

{
  "trainer": 1,
  "pokemon": 3
}

Remover relação
DELETE /api/trainer-pokemons/<id>/

3.4. PokeAPI Proxy

Busca informações diretamente da PokeAPI oficial.

GET /api/pokeapi/<pokemon_name>/


Exemplo de resposta:

{
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "photo": "https://raw.githubusercontent.com/.../pikachu.png"
}

3.5. Batalha Pokémon

Compara dois Pokémons pelo peso.

GET /api/battle/<pokemon1_id>/<pokemon2_id>/


Regras:

O Pokémon mais pesado vence.

Se o peso for igual → empate.

Se pertencerem ao mesmo treinador → erro.

Exemplo de respostas:

Vitória:

{
  "winner": "Snorlax",
  "loser": "Pikachu"
}


Empate:

{
  "result": "Empate! Ambos têm o mesmo peso."
}


Mesmo treinador:

{
  "error": "Os Pokémons pertencem ao mesmo treinador."
}