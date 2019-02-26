## codecentric.AI Bootcamp

Hier findest Du die Kursinhalte zum codecentric.AI Bootcamp (https://bootcamp.codecentric.ai).

## Anleitung für den Praxisteil des Bootcamps
Mit den folgenden Schritten kannst du den Code unserer Übungsaufgaben lokal ausführen.
**Wenn du Hilfe benötigst, schreib uns in unserer Slack Community an: https://join.slack.com/t/cc-ai-bootcamp/signup**

1. Setze eine Entwicklungsumgebung auf.
Um die Übungsaufgaben auszuführen, brauchst du eine Entwicklungsumgebung. In unserem Kurs findest du im Modul 2 eine
genaue Anleitung, wie man dies am besten einrichtet.

2. Installiere Git
Git benötigst du, um daraufhin den Code aus unserem Repository klonen zu können: https://git-scm.com/book/de/v1/Los-geht%E2%80%99s-Git-installieren

3. Installiere Docker
Um die Jupyter Notebooks lokal auf Deinem Rechner laufen zu lassen benötigst du Docker (https://docs.docker.com/install/).

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

  - **Auf Mac oder Linux:**

```bash
# Jupyter Server starten und Übungsaufgaben in den Container mounten
docker run -p 127.0.0.1:8888:8888 -v $(pwd)/notebooks:/notebooks -v $(pwd)/data:/data codecentric.ai-docker

# Aktuellen Stand der Datensätze laden
./run.sh
```
  - **Auf Windows:



```bash
# Jupyter Server starten und Übungsaufgaben in den Container mounten
docker run -p 8888:8888 -v %cd%/data:/data -v %cd%/notebooks:/notebooks codecentric/codecentric.ai-docker
```

Falls der Pfad mit `%cd%` nicht erkannt wird, verwende den absoluten Pfadnamen, zum Beispiel:

7. Installation testen & loslegen

Rufe `http://localhost:8888/` in deinem Browser auf.

Du siehst keine Übungsaufgaben? 
Vermutlich wurde nicht der richtige Pfad der Übungsaufgaben zum Container hinzugefügt. Achte darauf, dass du dich im Terminal (bzw. in der Shell) zuerst zum Ordner des Bootcamps wechselst, bevor du die Befehle ausführst.

```

## Übungsaufgaben auf Amazon Web Services (AWS) starten

Um die Deep Learning Aufgaben auszuführen, brauchst Du einen Rechner mit einer geeigneten Grafikkarte. In unserem Kurs
zeigen wir Dir, wie du einen AWS EC2 Instanz einrichten kannst, um dort unsere Docker Umgebung laufen lassen zu können.
