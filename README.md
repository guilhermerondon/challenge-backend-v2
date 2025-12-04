# 🐍 Pokémon API

API REST em Django + Django REST Framework para gerenciar Treinadores, Pokémons, Relações e Sistema de Batalha inspirado na franquia Pokémon.

Esse README foi escrito para que qualquer pessoa consiga rodar o projeto do zero, mesmo sem experiência prévia com Django.

## 📚 Índice

Descrição do Projeto

Tecnologias Utilizadas

Estrutura do Projeto

Instalação e Setup (Docker)

Rodando o Servidor

Endpoints da API

Coleção do Postman

Endpoints da API

Exemplos de Requests e Responses

Rodando os Testes

## 📝 Descrição do Projeto

Esta API permite:

✔️ Criar e gerenciar treinadores
✔️ Criar e gerenciar pokémons (com busca de atributos na PokeAPI)
✔️ Relacionar treinadores ↔ pokémons
✔️ Simular batalhas automáticas entre treinadores
✔️ Atribuir um pokémon vencedor baseado em atributos

O objetivo do desafio é demonstrar:

Boas práticas de Django

Arquitetura de API REST

Organização de apps

Estrutura limpa

CRUD completo

Testes automatizados

## 🛠 Tecnologias Utilizadas

Python 3.10+

Django 5

Django REST Framework

Banco de Dados PostgreSQL

Containers Docker e Docker Compose

Postman (testes da API)

VS Code


### 💿 Instalação e Setup
O ambiente completo (incluindo o servidor PostgreSQL) é configurado e inicializado via Docker Compose.

- Pré-requisitos (Ferramentas de Desenvolvimento):

1 - Git: Para clonar o repositório.

2 - Docker Desktop: Instalado e em execução (necessário para rodar os containers).

3 - VS Code (ou editor de sua preferência).


## 1. Clonar o Projeto
```
git clone https://github.com/SEU_USUARIO/challenge-backend.git
cd challenge-backend
```

## 2. Iniciar o Ambiente
O comando a seguir irá: construir a imagem Python (Dockerfile), instalar todas as dependências (incluindo psycopg2), iniciar o container PostgreSQL, rodar as migrações, e iniciar o servidor Django.

```
docker compose up -d --build
```


## 3. Verificar Status
Confirme que ambos os containers (postgres_db e django_pokemon_api) estão rodando:

```
docker compose ps
```

A API rodará em:
👉 http://localhost:8000/

## 🌐 Endpoints da API

| Módulo | Método | Rota | Descrição |
| :--- | :--- | :--- | :--- |
| **Treinadores** | GET, POST, PATCH, DELETE | `/trainers/` ou `/trainers/{id}/` | CRUD completo para gerenciar treinadores. |
| **Pokémons** | GET, POST, PATCH, DELETE | `/pokemons/` ou `/pokemons/{id}/` | CRUD completo. O **POST** inicia a busca de atributos (Peso, Altura, Foto) na PokeAPI. |
| **Relações** | POST | `/relations/add/` | Adiciona um Pokémon a um Treinador (requer `trainer_id` e `pokemon_id`). |
| **Relações** | DELETE | `/relations/remove/` | Remove a associação de um Pokémon com um Treinador (requer `trainer_id` e `pokemon_id`). |
| **Batalha** | POST | `/battle/{id1}/{id2}/` | Simula uma batalha entre dois Pokémons. **Ganha o Pokémon com maior peso.** |

## 🔗 Coleção do Postman

Coleção pública para testes de todos os endpoints (incluindo regras de batalha)

```
✅ https://elements.getpostman.com/redirect?entityId=37984684-2f49a341-212a-42c8-93b5-d34974dd3d65&entityType=collection
```

## 📜 Exemplos de Requests e Responses

### ➕ Adicionar Pokémon ao treinador
**POST /relations/add/1/25/**

```
{
  "id": 3,
  "trainer": 1,
  "pokemon": 25,
  "added_at": "2025-01-15T18:22:40Z"
}
```

### ⚔️ Simular Batalha
**POST /battle/1/2/**

```
{
  "winner": "Ash",
  "loser": "Misty",
  "pokemon_used": "Pikachu"
}
```

## 🧪 Rodando os Testes (Unitários e Integração)
Execute os testes diretamente no container do Django para garantir que a lógica e a integração (PokeAPI, regras de batalha) estejam corretas.

### 1. Comando de Execução: Use ```docker compose exec``` para rodar os testes em todas as aplicações (este comando resolve o problema de caminho):

```
docker compose exec app sh -c "cd challenge_backend && python manage.py test pokemons trainers relations battle"
```

### 2. Resultado Esperado: O sistema deve retornar OK (sucesso total).