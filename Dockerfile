# 1. Escolhe a imagem base (Python)
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências (requirements.txt)
COPY requirements.txt /app/

# 4. Instala as dependências (incluindo psycopg2, Django e DRF)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o restante do código para o container
COPY . /app/c

# 6. Comando padrão para iniciar a aplicação (opcional, pois já está no docker-compose)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]