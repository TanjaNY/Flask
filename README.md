
# Eine Flask-Anwendung erstellen

## Voraussetzungen:

- Git: [Download](https://git-scm.com/downloads)
- Anaconda: [Download](https://www.anaconda.com/download)
- Docker: [Download](https://www.docker.com/products/docker-desktop/)
- Python: [Download](https://www.python.org/downloads/)
- Visual Studio Code: [Download](https://code.visualstudio.com/download)

## Warum Flask?

Flask ist eine ausgezeichnete Wahl für die Entwicklung von ML- und AI-Anwendungen aus verschiedenen Gründen:
-1) Einfachheit und Flexibilität: Flask ist ein leichtgewichtiges Web-Framework mit einer einfachen und leicht verständlichen Struktur. Es bietet eine minimale und flexible Schnittstelle zum Erstellen von Web-Anwendungen, sodass Entwickler sich auf die Kernfunktionalität von ML/AI konzentrieren können, ohne von komplexen Web-Entwicklungsdetails überfordert zu werden.
-2) Modularität und Erweiterbarkeit: Flask bietet ein modulares Design, das Entwicklern das Hinzufügen von Komponenten und Erweiterungen auf Bedarf ermöglicht. Dies erleichtert die Integration verschiedener Machine-Learning-Bibliotheken und Tools wie TensorFlow, PyTorch, NumPy und scikit-learn in Ihre Flask-Anwendung.
-3) Entwicklung von RESTful-APIs: Flask ist gut für die Erstellung von RESTful-APIs geeignet, die als Kommunikationsgrundlage für ML- und AI-Anwendungen dienen können. Sie können Flask verwenden, um APIs zu erstellen, die Eingabedaten akzeptieren, ML/AI-Aufgaben ausführen und die verarbeiteten Ergebnisse an Clients oder andere Komponenten in Ihrem System zurückgeben.
-4) Integration mit Datenspeichern und Datenbanken: Flask unterstützt verschiedene Optionen für die Datenspeicherung, einschließlich SQL-Datenbanken (wie MySQL, PostgreSQL oder SQLite) und NoSQL-Datenbanken (wie MongoDB). Dies erleichtert das Speichern, Abrufen und Verarbeiten großer Datensätze, was für ML- und AI-Anwendungen essentiell ist.
-5) Flexibilität bei der Bereitstellung: Flask-Anwendungen können auf mehreren Plattformen und Cloud-Diensten bereitgestellt werden, einschließlich Heroku, AWS, Google Cloud Platform und Microsoft Azure. Diese Flexibilität ermöglicht Ihnen, Ihre ML/AI-Anwendung anhand der Anforderungen Ihrer Benutzer oder Kunden zu skalieren.
-6) Lebendige Community und Ökosystem: Flask verfügt über eine große und aktive Entwicklergemeinde, die zu seiner Entwicklung, der Erstellung von Erweiterungen und der Unterstützung beiträgt. Dies bedeutet, dass Sie Zugang zu zahlreichen Ressourcen, Tutorials und Bibliotheken haben, die Ihnen helfen können, die Entwicklung Ihrer ML/AI-Anwendung zu beschleunigen.
Zusammenfassend macht Flasks Einfachheit, Flexibilität, Erweiterbarkeit und die einfache Integration mit ML/AI-Bibliotheken es zu einer idealen Wahl für die Entwicklung von Machine-Learning- und künstlicher Intelligenz-Anwendungen.

## 1.Beschreibung der Anwendung
Diese Webanwendung wurde mit Flask, einem Python-Webframework, entwickelt. Sie dient als Kreisflächenrechner und ermöglicht es Benutzern, den Radius eines Kreises einzugeben und dessen Fläche zu berechnen. Die Berechnung basiert auf der Formel für die Fläche eines Kreises, nämlich 3.14159 * (Radius)^2.
Diese Anwendung bietet einen einfachen und benutzerfreundlichen Einstieg in die Welt der Python-Programmierung und Datenverarbeitung.
Die Anwendung verfügt über ein einfaches und benutzerfreundliches Interface. Auf der Homepage des Rechners geben die Nutzer den Radius des Kreises in ein Eingabefeld ein und klicken auf die Schaltfläche "Calculate". Anschließend überprüft die Anwendung, ob der eingegebene Radius eine positive Zahl ist, und zeigt die Fläche des Kreises an.
Die Webanwendung wird mit Docker kontainerisiert, sodass die Bereitstellung und der Betrieb einfacher sind. Die Datei "Dockerfile" wird verwendet, um das Docker-Image zu bauen, und die Datei "requirements.txt" enthält die notwendigen Python-Abhängigkeiten für die Anwendung.

## 2. GitHub-Repository klonen:

- Öffne die Kommandozeile (cmd) auf deinem Windows-Computer.
- Navigiere zu dem Verzeichnis, in das du die Anwendung klonen möchtest.
- Verwende den folgenden Befehl, um das Repository von GitHub zu klonen:

```bash
git clone https://github.com/TanjaNY/Flask.git
```

## 3. Flask-Umgebung erstellen:

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
- Anaconda ist nicht zwingend erforderlich, um eine Flask-App zu entwickeln. Du benötigst Anaconda, wenn du Data Science meistern möchtest. Im Fall, dass du dich gegen Anaconda entscheidest, werden die Befehle etwas anders aussehen.


```bash
python -m venv flask_env 
```


```bash
flask_env\Scripts\activate
```

## 4. Flask und Werkzeug installieren:

Flask und Werkzeug sind zwei Python-Pakete, die für die Webentwicklung verwendet werden.
Flask ist ein leichtgewichtiges Webframework für Python, das die Entwicklung von Webanwendungen und APIs erleichtert. Es bietet eine einfache und intuitive API, die Entwicklern ermöglicht, einfache, aber leistungsfähige Web-Apps schnell und effizient zu entwickeln.
Werkzeug ist eine Python-Bibliothek, die eine Sammlung von Werkzeugen und Bibliotheken für die Entwicklung von Webanwendungen bereitstellt. Es bietet Funktionen wie HTTP-Verwaltung, Anwendungsobjekte und Debugging-Funktionen, die in Flask und anderen Python-Webframeworks verwendet werden können.
Werkzeug stellt somit eine wichtige Infrastruktur für die Entwicklung von Web-Apps und APIs mit Python dar.


- In der aktivierten Conda-Umgebung führe die folgenden Befehle aus, um Flask und Werkzeug zu installieren:

```bash
pip install flask 
pip install Werkzeug 
```

## 5. Flask-Anwendung lokal ausführen:

- Navigiere zum Verzeichnis der geklonten Flask-Anwendung.
- Aktiviere die Conda-Umgebung mit dem Befehl:

```bash
flask_env\Scripts\activate
```
- Stare  die Flask-Anwendung
```bash
flask run
```

- Dadurch wird die Anwendung gestartet und ist standardmäßig unter http://localhost verfügbar. Die Adresse wird nach dem Start angezeigt.

<p>&nbsp;</p>

![](https://github.com/TanjaNY/Flask/blob/main/pics/Flask02.png?raw=true)

<p>&nbsp;</p>

-Öffne deinen Webbrowser und gib die Adresse [http://127.0.0.1:5000](http://127.0.0.1:5000) in die Adressleiste ein, um deine Anwendung zu sehen.
 Die Anwendung wird ungefähr wie folgt angezeigt (ohne die Firefox-Meldung :-))

 <p>&nbsp;</p>



<p><img src="https://github.com/TanjaNY/Flask/blob/main/pics/flask01.png" widht="100" height="200" alt="Flask App" &nbsp;&nbsp;&nbsp;&nbsp /></p>
<p>&nbsp;</p>

## 6. Anwendung containerisieren mit Docker:

Dockerfile und docker-compose  sind zwei Schlüsselkonzepte im Docker-Ökosystem für die Containerisierung von Anwendungen. Dockerfile ist eine Textdatei, die den Prozess der Erstellung eines Docker-Images definiert, während docker-compose ein Tool ist, mit dem mehrere Docker-Container mit nur einer Befehlszeile gestartet und verwaltet werden können. Beide Konzepte spielen eine entscheidende Rolle bei der Entwicklung, dem Testen und dem Bereitstellen von Anwendungen innerhalb von Containern.
Ein Dockerfile beginnt immer mit einer Basisimage-Anweisung und enthält Anweisungen wie COPY, ADD, RUN, CMD und ENTRYPOINT, die dem Entwickler erlauben, das Image nach seinen Anforderungen zu konfigurieren. Docker-compose verwendet eine YAML-Datei, in der die Container definiert sind, die eine Anwendung ausmachen, und ermöglicht Entwicklern, eine lokale Entwicklungsumgebung nahtlos nachzubilden.
Dockerfile und docker-compose tragen zur Beliebtheit und Leistungsfähigkeit der Containerisierung als Technologie für die moderne Softwareentwicklung bei. In Ihrem Verzeichnis finden Sie Beispiele für beide Dateien. Obwohl du für dieses Projekt nur das Dockerfile benötigst, wirst du für weitere Entwicklungen, wie das Hinzufügen einer Datenbank oder eines Webservers, auch docker-compose (oder compose.yaml) verwenden können.

So containersierst du die Anwendung:

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



## Dies ist deine erste containerisierte Web-Anwendung., Congratulations!
        
