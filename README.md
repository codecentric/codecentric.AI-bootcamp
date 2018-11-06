# codecentric.AI Bootcamp

Hier findest Du die Kursinhalte zum codecentric.AI Bootcamp. Um die Übungsaufgaben auszuführen, brauchst du eine
Entwicklungsumgebung. In unserem Kurs findest du im Modul 2 eine genaue Anleitung, wie man dies am besten einrichtet.

Um die Jupyter Notebooks lokal auf Deinem Rechner laufen zu lassen benötigst du Docker (https://docs.docker.com/install/).
Dann kannst du den Jupyter Server wie folgt starten:

## codecentric.AI Bootcamp in Docker starten

```bash
# Docker file aus git holen
git clone https://github.com/codecentric/codecentric.AI-docker.git && cd codecentric.AI-docker

# Docker Contaier mit Jupyter Server und benötigten Python Libraries bauen
docker build -t codecentric.ai-docker .

# Übungsaufgaben aus git clonen
cd ..
git clone https://github.com/codecentric/codecentric.AI-bootcamp && cd codecentric.AI-bootcamp

# Jupyter Server starten und Übungsaufgaben in Container mounten
docker run -p 127.0.0.1:8888:8888 -v $(pwd)/notebooks:/notebooks codecentric.ai-docker
```

Teste deine Installation indem du `http://localhost:8888/` in deinem Browser aufrufst. Wenn du keine Übungsaufgaben siehst,
dann hast du den notebooks Pfad nicht richtig in den Container gemountet. Achte darauf, dass du die Befehle genau wie oben
beschrieben in den Ordnern ausführst.

Bei Problemen, kannst Du in unserer Slack Community nach Hilfe fragen https://join.slack.com/t/cc-ai-bootcamp/signup


## Übungsaufgaben auf Amazon Web Services (AWS) starten

Um die Deep Learning Aufgaben auszuführen, brauchst Du einen Rechner mit einer geeigneten Grafikkarte. In unserem Kurs
zeigen wir Dir, wie du einen AWS EC2 Instanz einrichten kannst, um dort unsere Docker Umgebung laufen lassen zu können.