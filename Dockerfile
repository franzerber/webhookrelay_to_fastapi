FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# requirements.txt kopieren und Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# gesamten Quellcode ins Arbeitsverzeichnis kopieren
COPY . .

# main.py ausführen
CMD ["python", "main.py"]