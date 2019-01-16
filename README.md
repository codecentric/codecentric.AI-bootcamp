# codecentric.AI Bootcamp

Hier findest Du die Kursinhalte zum codecentric.AI Bootcamp (https://bootcamp.codecentric.ai).
Um die Übungsaufgaben auszuführen, brauchst du eineEntwicklungsumgebung. In unserem Kurs findest du im Modul 2 eine
genaue Anleitung, wie man dies am besten einrichtet.

Um die Jupyter Notebooks lokal auf Deinem Rechner laufen zu lassen benötigst du Docker (https://docs.docker.com/install/).
Dann kannst du den Jupyter Server wie folgt starten:

## codecentric.AI Bootcamp in Docker starten

Die Notebooks findest du in diesem Github Repository, das du wie folgt clonen (also auf deinen Rechner kopieren) kannst:

```bash
git clone https://github.com/codecentric/codecentric.AI-bootcamp
cd codecentric.AI-bootcamp
```

Das Dockerfile zu diesem Kurs liegt auf der Docker-Cloud. Du kannst es ganz einfach herunterladen und bauen mit:

```bash
docker pull codecentric/codecentric.ai-docker
```

### Run on Mac & Linux

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
