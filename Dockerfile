# Utilisez une image de base alpine avec Python préinstallé
FROM python:3.9-alpine

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de configuration et les dépendances du projet
COPY requirements.txt .
COPY .env .

# Installe les dépendances du projet
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    libffi-dev \
    openssl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# Copie le code source du projet dans le conteneur
COPY . .

# Copie le fichier SQLite dans le conteneur
COPY EverseedDB.sqlite3 .

# Expose le port sur lequel le serveur Django s'exécute
EXPOSE 8000

# Définit la commande pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]