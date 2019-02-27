## Praxisübungen des codecentric.AI Bootcamps

In diesem Repository findest Du die Praxisübungen des [codecentric.AI Bootcamps](https://bootcamp.codecentric.ai).

Um den Code der Praxisübungen auf deinem Rechner ausführen zu können, musst du zuerst eine Entwicklungsumgebung aufsetzen. Hierfür durchlaufe einfach Schritt für Schritt die Anleitung hier unten.

Falls du Hilfe benötigen solltest, chatte mit uns in unserer [Slack Community](https://join.slack.com/t/cc-ai-bootcamp/shared_invite/enQtNTQyMTk0MzM2OTMxLTNkODg2YzIwYjdhZGI4YmU3YWNhMDc4NmIwZmFmMmJiN2JiODM1M2EyYTQxZGNhZjQwOGIwMTRlMDlhYzg1YTI). Wir freuen uns auch sehr über Feedback zu deinen Erfahrungen.

Voraussetzungen:

- **Git** [installieren](https://git-scm.com/book/de/v1/Los-geht%E2%80%99s-Git-installieren)

- **Docker** [installieren](https://docs.docker.com/install/)

### Einrichtung der Entwicklungsumgebung (lokal)

```bash
#Klone den Code mit Übungsaufgaben auf deinen eigenen Rechner
git clone https://github.com/codecentric/codecentric.AI-bootcamp

#Wechsele in den Ordner des Repositories
cd codecentric.AI-bootcamp

#Lade nun das Docker-Image herunter
docker pull codecentric/codecentric.ai-docker
```

Die Entwicklungsumgebung ist jetzt eingerichtet. Du kannst sie nun jederzeit wie folgt starten und aufrufen:

### Entwicklungsumgebung starten

1. Starte den Server auf deinem Rechner

  - **Auf Mac oder Linux:**

```bash
# Server starten
sh run.sh
```
  - **Auf Windows:**

```bash
# Server starten
run
```

2. Los geht's!

Rufe `http://localhost:8888/` in deinem Browser auf.

Du siehst keine Übungsaufgaben?
Vermutlich wurde nicht der richtige Pfad der Übungsaufgaben zum Container hinzugefügt. Achte darauf, dass du dich im Terminal (bzw. in der Shell) zuerst zum Ordner des Bootcamps wechselst, bevor du die Befehle ausführst.

### Einrichtung der Entwicklungsumgebung (Cloud)

Für manche Übungsaufgaben empfiehlt es sich, geeignete Grafikkarte zu verwenden, um ein Training in überschaubarer Zeit abzuschließen. Falls die Grafikkarte deines Rechners dafür nicht ausreicht, kannst du die Übungsaufgaben in der Cloud ausführen. Wir verwenden hierfür Amazon Web Services (AWS). Im Kurs zeigen wir Dir, wie du einen AWS EC2 Instanz einrichten kannst, um dort unser Docker-Image einrichten zu können.
