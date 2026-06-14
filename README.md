# Desafio Backend PokeAPI

Este é o backend para gerenciamento de Treinadores e Pokémons, integrado com a PokeAPI (https://pokeapi.co/).

## Tecnologias Utilizadas
- Python 3.11+
- Django 5+
- Django Rest Framework
- PostgreSQL
- Redis (para Cache)
- Docker & Docker Compose

## Instalação e Execução

Para rodar o projeto localmente, você precisará do Docker e Docker Compose instalados.

1. Clone ou acesse o diretório do projeto.
2. Construa e inicie os containers:
```bash
docker-compose up --build -d
```
3. O servidor estará rodando em `http://localhost:8000/`.

> **Nota:** As migrações do banco de dados são executadas automaticamente ao iniciar o container.

## Executando os Testes

Para executar a suíte de testes unitários:
```bash
docker exec -it django_pokemon_api python challenge_backend/manage.py test apps
```

---

## APIs e Exemplos de Uso

Abaixo estão os endpoints disponíveis e exemplos de Request/Response.

### 1. Treinadores (Trainers)

#### **Criar Treinador**
`POST /trainers/`
```json
{
  "name": "Ash Ketchum",
  "age": 10
}
```
**Response (201 Created):**
```json
{
  "id": 1,
  "name": "Ash Ketchum",
  "age": 10,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

#### **Listar Treinadores** (Com Cache)
`GET /trainers/`

### 2. Pokémons

A aplicação consome a PokeAPI. Para criar um Pokémon, envie **apenas o nome**. Os demais atributos serão buscados automaticamente (com cache de 10 minutos para otimizar requisições).

#### **Criar Pokémon**
`POST /pokemons/`
```json
{
  "name": "pikachu"
}
```
**Response (201 Created):**
```json
{
  "id": 1,
  "name": "Pikachu",
  "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
  "height": 4,
  "weight": 60,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

#### **Listar Pokémons** (Com Cache)
`GET /pokemons/`

### 3. Relações (Treinadores e Pokémons)

#### **Listar Pokémons dos Treinadores** (Com Cache)
`GET /relations/`

#### **Adicionar Pokémon ao Treinador**
`POST /relations/add/`
```json
{
  "trainer_id": 1,
  "pokemon_id": 1
}
```
**Response (201 Created):**
```json
{
  "id": 1,
  "trainer": 1,
  "pokemon": 1,
  "added_at": "2023-10-01T12:05:00Z"
}
```

#### **Remover Pokémon do Treinador**
`DELETE /relations/remove/`
```json
{
  "trainer_id": 1,
  "pokemon_id": 1
}
```

### 4. Batalha (Battle)

Endpoint para verificar qual Pokémon vence um combate baseado em peso.
`GET /battle/<pokemon1_id>/<pokemon2_id>/`

**Cenário 1: P1 mais pesado (Vence P1)**
`GET /battle/1/2/` (Onde 1=Snorlax, 2=Pikachu)
**Response:**
```json
{
  "vencedor": "Snorlax"
}
```

**Cenário 2: Empate de peso**
**Response:**
```json
{
  "resultado": "empate"
}
```

**Cenário 3: Mesmo Treinador**
Se Snorlax e Pikachu pertencerem ao Ash:
**Response (400 Bad Request):**
```json
{
  "erro": "Pokémons do mesmo treinador. Eles não podem batalhar."
}
```