# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho na imagem
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do sistema necessárias para bcrypt
RUN apt-get update && apt-get install -y build-essential libffi-dev python3-dev

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante da aplicação para o diretório de trabalho
COPY . .

# Defina a variável de ambiente para o número de workers do Gunicorn
ENV WORKERS=4

# Comando para iniciar a aplicação
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8888"]
