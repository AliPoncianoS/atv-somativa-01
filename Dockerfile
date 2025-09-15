# Imagem base leve do Python
FROM python:3

# Pasta de trabalho dentro do container
WORKDIR /usr/src/app

# Copia apenas o requirements primeiro (melhora cache)
COPY requirements.txt ./

# Instala dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos
COPY . .

# Comando padrão ao iniciar o container
CMD ["python", "app.py"]