# Zugänglichkeitsprüfung mit Selenium und Azure Cognitive Services

Dieses Projekt bietet ein Skript zur Automatisierung der Zugänglichkeitsprüfung von Webseiten, indem es Bilder ohne Alternativtext identifiziert und mithilfe der Azure Cognitive Services Bildanalyse für diese Bilder Bildunterschriften generiert. Zusätzlich extrahiert es Informationen über fokussierbare Elemente auf der Webseite, um die Barrierefreiheit zu bewerten.
## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass folgende Werkzeuge auf Ihrem System installiert sind:

- Python 3.6 oder höher
- pip (Python Paketmanager)
- Google Chrome Browser
- Chrome WebDriver

## Setup

### Schritt 1: Repository Klonen

Klonen Sie das Repository auf Ihr lokales System mit:

```
git clone https://github.com/Roba42/EPWS2324-BrachtendorfHayaniKraft
```

Navigieren Sie in das Projektverzeichnis:

```
cd EPWS2324-BrachtendorfHayaniKraft

```

### Schritt 2: Virtuelle Umgebung Einrichten

(Optional) Erstellen Sie eine virtuelle Umgebung, um Konflikte mit anderen Projekten oder Systembibliotheken zu vermeiden:

```
python -m venv venv
```

Aktivieren Sie die virtuelle Umgebung:

- Windows:
  ```
  .\venv\Scripts\activate
  ```
- macOS/Linux:
  ```
  source venv/bin/activate
  ```

### Schritt 3: Abhängigkeiten Installieren

Installieren Sie die erforderlichen Python-Pakete mit:

```
pip install selenium azure-ai-vision-imageanalysis
```

### Schritt 4: Chrome WebDriver

Laden Sie den Chrome WebDriver herunter, der mit Ihrer Version von Google Chrome kompatibel ist. Sie können ihn von der offiziellen [Chrome WebDriver-Seite](https://sites.google.com/chromium.org/driver/) herunterladen.

Extrahieren Sie den heruntergeladenen WebDriver und platzieren Sie ihn in einem Verzeichnis Ihrer Wahl. Stellen Sie sicher, dass der Pfad zum WebDriver in Ihrem Systempfad enthalten ist, damit Selenium ihn finden kann.

### Schritt 5: Azure Cognitive Services Konfigurieren

Um die Bildanalyse durchzuführen, benötigen Sie einen Azure-Account und müssen die Bildanalysedienste einrichten. Folgen Sie der [offiziellen Anleitung](https://learn.microsoft.com/de-de/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0) um einen Schlüssel und einen Endpunkt für die Bildanalyse zu erhalten.

Konfigurieren Sie die Umgebungsvariablen `VISION_ENDPOINT` und `VISION_KEY` mit Ihrem Endpunkt und Schlüssel:

- Windows:
  ```
  set VISION_ENDPOINT=IhrEndpunkt
  set VISION_KEY=IhrSchlüssel
  ```
- macOS/Linux:
  ```
  export VISION_ENDPOINT=IhrEndpunkt
  export VISION_KEY=IhrSchlüssel
  ```

## Ausführung

Führen Sie das Skript mit dem folgenden Befehl aus:

```
python Accesstra.py
```

Das Skript öffnet automatisch den Chrome-Browser, navigiert zur angegebenen Webseite, analysiert die Zugänglichkeit und erstellt einen Bericht.

## Lizenz

[MIT](LICENSE)



