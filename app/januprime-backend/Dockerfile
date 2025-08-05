FROM python:3.13.5-slim

# 2. Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Definir o diretório de trabalho dentro do contentor
WORKDIR /app

# 4. Copiar o ficheiro de dependências
COPY requirements.txt .

# 5. Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar o código da aplicação para o contentor
COPY ./app /app