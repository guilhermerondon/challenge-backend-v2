# 🐍 Pokémon API

API REST em Django + Django REST Framework para gerenciar Treinadores, Pokémons, Relações e Sistema de Batalha inspirado na franquia Pokémon.

Esse README foi escrito para que qualquer pessoa consiga rodar o projeto do zero, mesmo sem experiência prévia com Django.

## 📚 Índice

Descrição do Projeto

Tecnologias Utilizadas

Estrutura do Projeto

Instalação e Setup

Rodando o Servidor

Coleção do Postman

Endpoints da API

Exemplos de Requests e Responses

Rodando os Testes

## 📝 Descrição do Projeto

Esta API permite:

✔️ Criar e gerenciar treinadores
✔️ Criar e gerenciar pokémons
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

SQLite (padrão do Django)

Postman (testes da API)

VS Code


### 💿 Instalação e Setup

```
✔️ 1. Instalar Python

https://www.python.org/downloads/

⚠️ Marque “Add Python to PATH”
```

```
✔️ 2. Instalar Git

https://git-scm.com/downloads
```


```
✔️ 3. Instalar VS Code

https://code.visualstudio.com/
```

### Extensões recomendadas:

Python

Django

## 📥 4. Clonar o Projeto
```
git clone https://github.com/SEU_USUARIO/challenge-backend.git
cd challenge-backend
```

###  🧱 Criar Ambiente Virtual (Recomendado)
Windows
python -m venv venv
venv\Scripts\activate

Linux/Mac
python -m venv venv
source venv/bin/activate


## 📦 5. Instalar Dependências

```
**pip install -r requirements.txt**
```

Dependências instaladas automaticamente:
```
Django 5.x

Django REST Framework

TZdata

Outras libs necessárias ao projeto
```

## 📁 6. Entrar na pasta do projeto Django
**cd challenge_backend**

## 🛠 7. Criar Banco de Dados
**python manage.py migrate**

## ▶️ 8. Rodar o Servidor
**python manage.py runserver**


# A API rodará em:

👉 http://127.0.0.1:8000/

🔗 Coleção do Postman
Collection pública para testes:

```
✅ https://elements.getpostman.com/redirect?entityId=37984684-2f49a341-212a-42c8-93b5-d34974dd3d65&entityType=collection
```

Inclui:

CRUD completo de Treinadores

CRUD completo de Pokémons

Relações

Batalha

Ambiente com variável base_url

Exemplos de requests prontos

## 🌐 Endpoints da API

👤 Treinadores
Método	Rota	Descrição
GET	/trainers/	Lista treinadores
POST	/trainers/	Cria treinador
GET	/trainers/{id}/	Detalhes
PUT	/trainers/{id}/	Edita
DELETE	/trainers/{id}/	Remove

🐾 Pokémons
Método	Rota	Descrição
GET	/pokemons/	Lista
POST	/pokemons/	Cria
GET	/pokemons/{id}/	Detalhes
PUT	/pokemons/{id}/	Edita
DELETE	/pokemons/{id}/	Remove

🔗 Relação Treinador ↔ Pokémon
Método	Rota	Função
POST	/relations/add/{trainer_id}/{pokemon_id}/	Adiciona
DELETE	/relations/remove/{trainer_id}/{pokemon_id}/	Remove

⚔️ Batalha Pokémon
Método	Rota	Descrição
POST	/battle/{trainer1}/{trainer2}/	Simula batalha


##  📜 Exemplos de Requests e Responses
➕ Adicionar Pokémon ao treinador
POST /relations/add/1/25/


Resposta
```
{
  "id": 3,
  "trainer": 1,
  "pokemon": 25,
  "added_at": "2025-01-15T18:22:40Z"
}
```

⚔️ Simular Batalha
POST /battle/1/2/


Resposta
```
{
  "winner": "Ash",
  "loser": "Misty",
  "pokemon_used": "Pikachu"
}
```

# 🧪 Rodando os Testes

python manage.py test


Os testes cobrem:

Trainers

Pokémons

Relações

Batalha
