FROM python:3.8-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SQLALCHEMY_SILENCE_UBER_WARNING=1

# Instalar dependencias del sistema incluyendo curl para healthchecks
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar código fuente
COPY . .

# NO entrenar modelo aquí - se hará con el servicio rasa-train

# Exponer puertos
EXPOSE 5005 5055

# El comando se define en docker-compose.yml