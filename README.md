## codecentric.AI Bootcamp

Hier findest Du die Kursinhalte zum codecentric.AI Bootcamp (https://bootcamp.codecentric.ai).

## Anleitung, um deine Übungsaufgaben lokal lösen zu können

1. Setze eine Entwicklungsumgebung auf.
Um die Übungsaufgaben auszuführen, brauchst du eine Entwicklungsumgebung. In unserem Kurs findest du im Modul 2 eine
genaue Anleitung, wie man dies am besten einrichtet.

2. Installiere Git
Git benötigst du, um daraufhin den Code aus unserem Repository klonen zu können: https://git-scm.com/book/de/v1/Los-geht%E2%80%99s-Git-installieren

3. Installiere Docker
Um die Jupyter Notebooks lokal auf Deinem Rechner laufen zu lassen benötigst du Docker (https://docs.docker.com/install/).

(Führe folgende Befehle in der Kommandozeile aus)

4. Klone den Code mit Übungsaufgaben auf deinen eigenen Rechner.

```bash
git clone https://github.com/codecentric/codecentric.AI-bootcamp
cd codecentric.AI-bootcamp
```

5. Installiere das Docker-Image.

```bash
docker pull codecentric/codecentric.ai-docker
```

6. Starte den Server auf deinem Rechner

  - Auf Mac oder Linux

Den Jupyter Server starten und die Übungsaufgaben und Daten in den Container mounten kannst du mit Mac und Linux so:

```bash
# Jupyter Server starten und Übungsaufgaben in Container mounten
docker run -p 127.0.0.1:8888:8888 -v $(pwd)/notebooks:/notebooks -v $(pwd)/data:/data codecentric.ai-docker

# Daten laden
./run.sh
```

### Run on Windows

Den Jupyter Server starten und die Übungsaufgaben und Daten in den Container mounten kannst du mit Windows so (falls er den Pfad mit `%cd%` nicht erkennt, musst du hier den absoluten Pfadnamen angeben):

```bash
docker run -p 8888:8888 -v %cd%/data:/data -v %cd%/notebooks:/notebooks codecentric/codecentric.ai-docker
```

## Jupyter Lab starten

Teste deine Installation indem du `http://localhost:8888/` in deinem Browser aufrufst. Wenn du keine Übungsaufgaben siehst,
dann hast du den notebooks Pfad nicht richtig in den Container gemountet. Achte darauf, dass du die Befehle genau wie oben
beschrieben in den Ordnern ausführst.

**Bei Problemen, kannst Du in unserer Slack Community nach Hilfe fragen https://join.slack.com/t/cc-ai-bootcamp/signup**


## Build locally

Alternativ kannst du das Dockerimage auch lokal bei dir bauen (wenn du zum Beispiel etwas hinzufügen oder verändern möchtest).

```bash
# Docker file aus git holen
git clone https://github.com/codecentric/codecentric.AI-docker.git && cd codecentric.AI-docker

# Docker Container mit Jupyter Server und benötigten Python Libraries bauen
docker build -t codecentric.ai-docker .

# Übungsaufgaben aus git clonen
git clone https://github.com/codecentric/codecentric.AI-bootcamp.git && cd codecentric.AI-bootcamp

# Jupyter Server starten und Übungsaufgaben in Container mounten
docker run -p 127.0.0.1:8888:8888 -v $(pwd)/notebooks:/notebooks -v $(pwd)/data:/data codecentric.ai-docker
```

## Übungsaufgaben auf Amazon Web Services (AWS) starten

Um die Deep Learning Aufgaben auszuführen, brauchst Du einen Rechner mit einer geeigneten Grafikkarte. In unserem Kurs
zeigen wir Dir, wie du einen AWS EC2 Instanz einrichten kannst, um dort unsere Docker Umgebung laufen lassen zu können.
