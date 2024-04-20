
# Eine Flask-Anwendung erstellen

## Voraussetzungen:

- Git: [Download](https://git-scm.com/downloads)
- Anaconda: [Download](https://www.anaconda.com/download)
- Docker: [Download](https://www.docker.com/products/docker-desktop/)
- Python: [Download](https://www.python.org/downloads/)
- Visual Studio Code: [Download](https://code.visualstudio.com/download)

## 1. GitHub-Repository klonen:

- Öffne die Kommandozeile (cmd) auf deinem Windows-Computer.
- Navigiere zu dem Verzeichnis, in das du die Anwendung klonen möchtest.
- Verwende den folgenden Befehl, um das Repository von GitHub zu klonen:

```bash
git clone https://github.com/TanjaNY/Flask.git
```

## 2. Conda-Umgebung erstellen:

- Öffne die Conda-Befehlszeile.
- Füge dein Anaconda-Verzeichnis zu den Umgebungsvariablen hinzu [Anleitung](https://michster.de/wie-setze-ich-die-path-umgebungsvariablen-unter-windows-10/).
- Verwende den folgenden Befehl, um eine neue Conda-Umgebung zu erstellen:

```bash
conda create --name flask_env 
```

- Aktiviere die erstellte Umgebung mit dem Befehl:

```bash
conda activate flask_env 
```

## 3. Flask und Werkzeug installieren:

- In der aktivierten Conda-Umgebung führe die folgenden Befehle aus, um Flask und Werkzeug zu installieren:

```bash
pip install flask 
pip install Werkzeug 
```

## 4. Flask-Anwendung lokal ausführen:

- Navigiere zum Verzeichnis der geklonten Flask-Anwendung.
- Öffne eine Befehlszeile im Verzeichnis der Anwendung.
- Aktiviere die Conda-Umgebung mit dem Befehl:

```bash
flask run
```

- Dadurch wird die Anwendung gestartet und ist standardmäßig unter http://localhost verfügbar. Die Adresse wird nach dem Start angezeigt.

![](pics/flask00)

## 5. Anwendung containerisieren mit Docker:

- Installiere und starte Docker-Desktop.
- Stelle sicher, dass sich die Dateien Dockerfile und docker-compose.yml im Stammverzeichnis der Anwendung befinden.
- Bulde das Docker Image.

```bash
Docker build -t myflask-app:latest
```

- Führe den folgenden Befehl aus, um die Anwendung mit Docker lokal auszuführen:

```bash
docker-compose up -d
```

- Dadurch wird die Anwendung in einem Docker-Container gestartet und ist unter der angegebenen Adresse http://localhost:5004 verfügbar.



## Das ist deine erste Web-Anwendung, Congratulations!
        
