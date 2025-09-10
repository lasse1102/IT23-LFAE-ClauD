### Infoblatt: Docker Compose

#### Was ist Docker Compose?

Docker Compose ist ein Werkzeug, das es ermöglicht, Multi-Container-Docker-Anwendungen zu definieren und auszuführen. Mit einem einzigen Befehl können alle Dienste einer Anwendung gestartet werden, die in einem YAML-Format beschrieben sind. Es vereinfacht die Verwaltung komplexer Anwendungen, indem es die Konfiguration und den Startprozess automatisiert.

#### Warum Docker Compose verwenden?

1. **Vereinfachte Verwaltung von Container-Anwendungen**: Mit Docker Compose können mehrere Container gleichzeitig gestartet, gestoppt und verwaltet werden.
2. **Portabilität**: Anwendungen können auf verschiedenen Umgebungen (Entwicklung, Test, Produktion) mit denselben Konfigurationen ausgeführt werden.
3. **Automatisierung**: Reduzierter manueller Aufwand durch automatische Erstellung und Verwaltung von Netzwerken und Volumes.
4. **Schnelles Setup**: Entwicklungsumgebungen können schnell eingerichtet werden.

#### Grundlegende Konzepte

- **YAML-Datei (`docker-compose.yml`)**: Eine Textdatei im YAML-Format definiert die Services, Netzwerke und Volumes der Anwendung.
- **Services**: Jeder Service entspricht einem Container oder einer Gruppe von Containern mit derselben Konfiguration.
- **Netzwerke**: Ermöglichen die Kommunikation zwischen Containern.
- **Volumes**: Persistente Speicherorte zur Datenspeicherung außerhalb des Containers.

#### Grundstruktur einer `docker-compose.yml`

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: example
```

Dieser einfache Aufbau definiert zwei Services – einen Webserver (nginx) und eine Datenbank (MySQL).

#### Wichtige Befehle

- `docker-compose up`: Startet alle im YAML definierten Services. Mit dem Flag `-d` wird im Hintergrundmodus gestartet.
- `docker-compose down`: Stoppt alle laufenden Services und entfernt Container sowie Netzwerke, aber nicht definierte Volumes.
- `docker-compose ps`: Zeigt den Status der laufenden Services an.
- `docker-compose logs`: Zeigt Logs der laufenden Container an.

#### Best Practices

1. **Modularisierung der Konfigurationen**:
   
   - Trennen Sie Entwicklungs-, Test- und Produktionskonfigurationen in verschiedene Dateien oder verwenden Sie Variablen für dynamische Werte.

2. **Verwendung von Umgebungsvariablen**:
   
   - Sensible Informationen wie Passwörter sollten über Umgebungsvariablen gesteuert werden.

3. **Netzwerkisolation**:
   
   - Nutzen Sie separate Netzwerke für unterschiedliche Teile Ihrer Anwendung zur Erhöhung der Sicherheit.

4. **Persistenz beachten**:
   
   - Verwenden Sie Volumes für persistente Daten, um Datenverlust beim Neustart von Containern zu vermeiden.

5. **Versionierung der Compose-Datei**:
   
   - Nutzen Sie eine Versionskontrolle für Ihre `docker-compose.yml`, um Änderungen nachvollziehbar zu machen.

#### Fazit

Docker Compose ist ein mächtiges Werkzeug zur Verwaltung komplexer Anwendungen in Containern. Durch seine Fähigkeit, mehrere Dienste gleichzeitig zu starten, ermöglicht es eine effizientere Entwicklungspipeline und erleichtert das Deployment in unterschiedlichen Umgebungen erheblich.

### Übung 1: Einfaches Web-Setup

**Aufgabe:**  
Erstelle eine `docker-compose.yml`-Datei, die einen einfachen Webserver (nginx) bereitstellt. Der Webserver soll über Port 8080 erreichbar sein. Diese Übung ist ähnlich unserer vorherigen reinen Docker-Installation.

**Schritte:**

1. Erstelle ein Verzeichnis für dein Projekt.
2. Erstelle eine `docker-compose.yml`-Datei in diesem Verzeichnis.
3. Definiere einen Service für den nginx-Webserver.
4. Mappe den Container-Port 80 auf den Host-Port 8080.
5. Starte den Container mit Docker Compose und überprüfe, ob der Webserver über `http://localhost:8080` erreichbar ist.

### Übung 2: Mehrere Dienste und Netzwerk

**Aufgabe:**  
Erweitere dein Setup um einen MySQL-Datenbank-Service, der mit dem nginx-Webserver kommunizieren kann.

**Schritte:**

1. Ergänze die bestehende `docker-compose.yml` um einen neuen Service für MySQL.
2. Stelle sicher, dass die Dienste über ein gemeinsames Netzwerk kommunizieren können (automatisch durch Docker Compose).
3. Verwende Umgebungsvariablen zur Konfiguration des MySQL-Datenbank-Passworts (s. o.).
4. Überprüfe die Kommunikation zwischen nginx und MySQL.

### Übung 3: Persistente Daten

**Aufgabe:**  
Stelle sicher, dass deine MySQL-Datenbank auch nach einem Neustart des Containers bestehen bleibt.

**Schritte:**

1. Füge in der `docker-compose.yml` ein Volume hinzu, das die Datenbankdaten speichert.
2. Starte die Dienste neu und überprüfe, ob die Daten persistent gespeichert werden (z.B., indem du eine Testdatenbank erstellst und nach einem Neustart darauf zugreifst).

### Übung 4: Logs und Fehlerbehebung

**Aufgabe:**  
Analysiere Log-Dateien, um Fehler im System zu identifizieren und zu beheben.

**Schritte:**

1. Starte deine Docker-Compose-Anwendung.
2. Führe Aktionen aus, die bewusst zu Fehlern führen könnten (wie falsche Zugangsdaten).
3. Verwende den Befehl `docker-compose logs`, um die Log-Dateien beider Services zu überprüfen.
4. Identifiziere potenzielle Probleme anhand der Logs und beschreibe mögliche Lösungsansätze.

### Übung 5: Modularisierung und Best Practices

**Aufgabe:**  
Modularisiere deine Konfigurationen für Entwicklungs- und Produktionsumgebungen.

**Schritte:**

1. Erstelle separate `docker-compose.dev.yml` und `docker-compose.prod.yml` Dateien basierend auf deiner aktuellen Konfiguration.
2. Verwende Umgebungsvariablen oder `.env` Dateien, um unterschiedliche Werte in Entwicklung und Produktion zu setzen (z.B., Debugging-Einstellungen oder Datenbankverbindungen).
3. Teste beide Setups lokal, indem du das entsprechende Compose-File angibst (`-f` Flag) beim Starten von Docker Compose.
