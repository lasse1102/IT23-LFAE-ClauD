### Container-Dienste mit Docker und Kubernetes 

## Ausgangssituation und Projektszenario

Die Auszubildenden übernehmen die Rolle von IT-Dienstleistern, die für einen fiktiven Kunden, die TechConnect GmbH, eine containerisierte Anwendungsumgebung realisieren sollen. Der Kunde betreibt aktuell eine monolithische PHP-Anwendung mit MySQL-Datenbank auf einem einzelnen Server, die bei höherer Auslastung Performance-Probleme zeigt und bei Updates Ausfallzeiten erfordert. Die Geschäftsführung wünscht eine zukunftssichere und hochverfügbare IT-Infrastruktur.

### Kundenanforderungen

- Migration der bestehenden Anwendung in eine containerisierte Umgebung
- Trennung von Frontend, Backend und Datenbank in unabhängige Komponenten
- Automatische Skalierung bei erhöhter Nutzerlast
- Minimierung von Ausfallzeiten bei Updates (Zero-Downtime-Deployments)
- Implementierung eines Monitoring- und Logging-Systems
- Vollständige technische Dokumentation der Lösung

## Sequenzplanung

### Stunde 1-2: Einführung und Anforderungsanalyse

**Material**: [[01 - Container & Kubernets]]

**Lernziele:**
- Grundprinzipien der Containerisierung verstehen
- Docker und Kubernetes konzeptionell unterscheiden können
- Eine strukturierte Anforderungsanalyse durchführen

**Materialien:**
- Video zu den Grundlagen der Containerisierung: [[01 - Container & Kubernets]]
- [[00 - Fallbeschreibung TechConnect GmbH]]
- [[01a - Anforderungsanalyse Vorlage]]

**Ablauf:**
1. Theoretische Einführung in Containerisierung vs. Virtualisierung (30 min)
   - Definition von Containern und deren Vorteile
   - Architektur von Container-Lösungen
   - Docker und Kubernetes im Überblick --> [[01 - Container & Kubernets]] ganz unten

2. Vorstellung des Kundenszenarios (20 min)
   - Ausgangssituation TechConnect GmbH
   - Problemstellungen und Anforderungen

3. Gruppenarbeit: Anforderungsanalyse (40 min)
   - Bildung von Projektteams (3-4 Personen) -> Wir bilden ein Team
   - Analyse der Kundenanforderungen
   - Erstellung eines ersten Lösungsansatzes --> dafür Recherche

4. Präsentation und Diskussion der Lösungsansätze (30 min)

**Aufgabe für die Auszubildenden:**
1. Analysieren Sie die IT-Infrastruktur der TechConnect GmbH.
2. Identifizieren Sie die konkreten Probleme und leiten Sie daraus Anforderungen ab.
3. Skizzieren Sie einen ersten Lösungsansatz mit containerisierter Architektur.
4. Präsentieren Sie Ihren Ansatz in 3-5 Minuten vor der Klasse.

### Stunde 3-4: Docker-Grundlagen und erste Container

**Lernziele:**
- Docker-Umgebung einrichten und grundlegende Befehle anwenden
	- WSL (Ubuntu / Debian)
	- Docker installieren
- Docker-Images erstellen und verwalten können
	- Video (s. o.) und Tutorials: https://docs.docker.com/get-started/introduction/
- Erste Container für die Kundenanwendung entwickeln

**Materialien:**
- Handout [[01b - Docker Cheat Sheet]]
- Installation-Guide für Docker (abhängig vom Betriebssystem) -> https://www.docker.com/get-started/
- [[01c - Übungsaufgaben Docker Container]]
- - Beispiel-Dockerfiles für Web-Anwendungen
	- Nginx: https://www.docker.com/blog/how-to-use-the-official-nginx-docker-image/
	- PHP: https://hub.docker.com/_/php


**Ablauf:**
1. Installation und Einrichtung von Docker (30 min)[18]
   - Docker Desktop/Docker Engine installieren und testen
   - Grundlegende Befehle (docker run, docker ps, docker images)
   - Docker Hub und öffentliche Images

2. Arbeiten mit Dockerfiles (40 min)[11][12]
   - Aufbau eines Dockerfiles --> Video Docker Tutorial, Cheat Sheet
   - Schichten-Konzept verstehen
	   - Recherche - Tipp: Verwendet eine KI, um Euch das Konzept erklären zu lassen (Lernen durch LLM-Einsatz)

3. Praktische Übung (50 min)
   - Übungsaufgaben
   - Erstellung eines Docker-Images für einen Webserver (nginx)
   - Konfiguration und Parameter anpassen
   - Container starten und testen

**Aufgabe für die Auszubildenden:**
1. Installieren Sie Docker auf Ihrem Entwicklungssystem.
2. Bearbeiten Sie die [[01c - Übungsaufgaben Docker Container]]
3. Erstellen Sie ein Dockerfile für einen Nginx-Webserver, der eine einfache Startseite für die TechConnect GmbH ausliefert. (Link siehe oben)
4. Bauen Sie das Image und starten Sie einen Container.
5. Implementieren Sie ein zweites Dockerfile für die PHP-Anwendung des Kunden. (Link siehe oben)
6. Dokumentieren Sie Ihre Schritte und Entscheidungen in einem Entwicklerlogbuch.

### Stunde 5-6: Mehrschichtige Anwendungen mit Docker Compose

**Lernziele:**
- Konzept von Multi-Container-Anwendungen verstehen
- Docker Compose zur Definition komplexer Anwendungen nutzen
- Netzwerke und Volumes für persistente Datenhaltung einsetzen

**Materialien:**
- Infoblatt [[02 - Docker Compose]]
- Vorlage für docker-compose.yml
- Beispielkonfiguration für LAMP/LEMP-Stack
- Diagramm zur Containerarchitektur

**Ablauf:**
1. Einführung in Docker Compose (30 min)[18]
   - Aufbau einer docker-compose.yml
   - Dienste definieren und verknüpfen
   - Abhängigkeiten zwischen Containern

2. Netzwerke und Volumes in Docker (30 min)[12]
   - Container-Kommunikation über Netzwerke
   - Persistente Datenspeicherung mit Volumes
   - Sicherheitsaspekte bei der Konfiguration

3. Praktisches Projektarbeit (60 min)
   - Erstellung einer docker-compose.yml für die TechConnect-Anwendung
   - Integration von Webserver, PHP-Anwendung und Datenbank
   - Testdaten importieren und Funktionalität überprüfen

**Aufgabe für die Auszubildenden:**
1. Erstellen Sie eine docker-compose.yml für eine dreischichtige Anwendung bestehend aus:
   - Nginx als Webserver/Reverse Proxy
   - PHP-Container für die Anwendungslogik
   - MySQL-Datenbank für Kundendaten
2. Konfigurieren Sie Volumes für die persistente Speicherung der Datenbank und Anwendungsdateien.
3. Implementieren Sie ein internes Netzwerk zur sicheren Kommunikation der Container.
4. Starten und testen Sie die gesamte Anwendung mit Docker Compose.
5. Dokumentieren Sie Ihre Konfiguration und erläutern Sie die Architekturentscheidungen.

### Stunde 7-8: Kubernetes-Grundlagen und Orchestrierung

**Lernziele:**
- Die Grundkonzepte von Kubernetes verstehen
- Kubernetes-Ressourcen definieren und anwenden können
- Die Vorteile der Container-Orchestrierung für den Kundenfall erkennen

**Materialien:**
- Kubernetes-Architekturdiagramm
- Installation-Guide für Minikube/k3s
- Beispielmanifeste für Deployments und Services
- Vergleichstabelle Docker Swarm vs. Kubernetes[3]

**Ablauf:**
1. Einführung in Kubernetes-Architektur (30 min)[5][7]
   - Control-Plane und Worker-Nodes
   - Grundlegende Ressourcentypen (Pods, Deployments, Services)
   - Kubernetes-Konzepte (Deklarativ, Self-Healing, Skalierung)

2. Lokale Kubernetes-Umgebung einrichten (30 min)
   - Installation von Minikube oder k3s
   - kubectl-Befehle
   - Namespaces und Kontexte

3. Praktische Übung (60 min)
   - Erstellen von Kubernetes-Manifesten für die TechConnect-Anwendung
   - Deployment der Container auf dem lokalen Cluster
   - Skalierung und Service-Konfiguration

**Aufgabe für die Auszubildenden:**
1. Richten Sie eine lokale Kubernetes-Umgebung mit Minikube oder k3s ein.
2. Erstellen Sie YAML-Manifeste für:
   - Deployments der Webserver-, PHP- und Datenbankcontainer
   - Services zur Kommunikation zwischen den Komponenten
   - ConfigMaps für Konfigurationsdateien
   - Secrets für Datenbank-Credentials
3. Deployen Sie die Anwendung auf Ihrem lokalen Kubernetes-Cluster.
4. Implementieren Sie eine horizontale Skalierung für den Webserver.
5. Testen Sie das Self-Healing durch simulierten Ausfall eines Pods.

### Stunde 9: Monitoring, Logging und Continuous Deployment

**Lernziele:**
- Monitoring- und Logging-Lösungen für containerisierte Anwendungen einrichten
- Continuous Deployment-Konzepte verstehen
- Zero-Downtime-Updates implementieren

**Materialien:**
- Konfigurationsbeispiele für Prometheus und Grafana
- Checkliste für Zero-Downtime-Deployments
- Diagramm einer CI/CD-Pipeline für Kubernetes

**Ablauf:**
1. Monitoring und Logging in Kubernetes (30 min)
   - Prometheus und Grafana als Monitoring-Lösung
   - EFK-Stack (Elasticsearch, Fluentd, Kibana) für Logging
   - Health-Checks und Readiness-Probes[5][7]

2. Continuous Deployment und Update-Strategien (20 min)[11]
   - Rolling Updates
   - Blue-Green Deployments
   - Canary Releases

3. Projektarbeit (40 min)
   - Implementation von Health-Checks für die Anwendungskomponenten
   - Konfiguration von Update-Strategien
   - Erstellung eines einfachen Monitoring-Dashboards

**Aufgabe für die Auszubildenden:**
1. Implementieren Sie Liveness- und Readiness-Probes für Ihre Kubernetes-Deployments.
2. Konfigurieren Sie eine Rolling-Update-Strategie mit Zero-Downtime-Deployment.
3. Integrieren Sie ein einfaches Monitoring mit Prometheus und Grafana.
4. Erstellen Sie ein Dashboard zur Überwachung der wichtigsten Metriken.
5. Dokumentieren Sie Ihre Monitoring- und Update-Strategie.

### Stunde 10: Projektabschluss und Präsentation

**Lernziele:**
- Eine professionelle Präsentation der Lösung erstellen und halten
- Die technische Dokumentation vervollständigen
- Das Projektergebnis kritisch reflektieren

**Materialien:**
- Vorlage für die technische Dokumentation
- Bewertungsbogen für die Präsentation
- Reflexionsfragebogen

**Ablauf:**
1. Fertigstellung der Dokumentation (20 min)
   - Vervollständigung der technischen Dokumentation
   - Erstellung einer Systemdokumentation für den Kunden
   - Vorbereitung der Präsentation

2. Präsentationen der Projektgruppen (40 min)
   - Jede Gruppe präsentiert ihre Lösung (5-10 min pro Gruppe)
   - Demo der implementierten Anwendung
   - Erläuterung der Architekturentscheidungen

3. Feedback und Reflexion (30 min)
   - Peer-Feedback zu den Präsentationen
   - Diskussion der unterschiedlichen Lösungsansätze
   - Reflexion des Lernprozesses

**Aufgabe für die Auszubildenden:**
1. Erstellen Sie eine vollständige technische Dokumentation Ihrer Containerarchitektur.
2. Bereiten Sie eine 5-10-minütige Präsentation vor, die folgende Aspekte abdeckt:
   - Architekturüberblick der Containerlösung
   - Erfüllung der Kundenanforderungen
   - Demonstration der Funktionalität
   - Skalierungs- und Update-Strategien
3. Präsentieren Sie Ihre Lösung vor der Klasse und beantworten Sie Fragen.
4. Reflektieren Sie schriftlich Ihren Lernprozess und identifizieren Sie Verbesserungspotenziale.

## Bewertungskriterien

Die Bewertung des Projekts erfolgt nach folgenden Kriterien:

1. **Technische Umsetzung (40%)**
   - Korrekte Implementierung der Docker-Container
   - Funktionsfähige Kubernetes-Konfiguration
   - Skalierbarkeit und Robustheit der Lösung
   - Monitoring- und Update-Mechanismen

2. **Konzeptionelle Qualität (30%)**
   - Erfüllung der Kundenanforderungen
   - Architekturdesign und Begründung der Entscheidungen
   - Berücksichtigung von Sicherheitsaspekten
   - Effizienz und Best Practices

3. **Dokumentation (20%)**
   - Vollständigkeit der technischen Dokumentation
   - Klarheit und Verständlichkeit
   - Anleitungen für Installation und Wartung
   - Berücksichtigung von Datenschutz und -sicherheit[9]

4. **Präsentation (10%)**
   - Strukturierte Darstellung der Lösung
   - Überzeugender Vortragsstil
   - Demonstration der Funktionalität
   - Beantwortung von Fachfragen

## Zusätzliche Materialien

### Projektmappe für Auszubildende

Jedes Projektteam erhält zu Beginn eine digitale Projektmappe mit:

- Detaillierte Kundenanforderungen und Ausgangssituation
- Zeitplan mit Meilensteinen für die 10-stündige Sequenz
- Checkliste für die zu implementierenden Features
- Vorlagen für Dokumentation und Projektbericht
- Links zu relevanten Ressourcen (Docker, Kubernetes Dokumentation)

### Technische Vorlagen und Beispiele

- Basis-Dockerfiles für die verschiedenen Anwendungskomponenten
- Beispiel docker-compose.yml für eine dreischichtige Anwendung
- Kubernetes-Manifest-Vorlagen für Deployments, Services, etc.
- Beispiel-Konfigurationen für Monitoring-Tools

### Hilfestellungen und Ressourcen

- Docker-Cheatsheet mit wichtigen Befehlen[18]
- Kubernetes-Architekturdiagramm[7]
- Fehlerbehebungsleitfaden für häufige Probleme
- Liste empfohlener Best Practices für containerisierte Anwendungen[11][12]

## Fazit

Diese Unterrichtssequenz bietet einen praxisnahen Einstieg in moderne Containertechnologien und deckt die im Rahmenlehrplan für Fachinformatiker im 3. Ausbildungsjahr geforderten Kompetenzen ab[10][13][15]. Die Auszubildenden durchlaufen alle Phasen eines realistischen IT-Projekts von der Anforderungsanalyse bis zur Präsentation der Lösung und erwerben dabei sowohl technisches Fachwissen als auch methodische und soziale Kompetenzen.

Die Sequenz ist so konzipiert, dass sie aktuelles Wissen in einem zukunftsrelevanten Themenfeld vermittelt und zugleich die berufliche Handlungsfähigkeit im Bereich der kundenspezifischen Systemintegration fördert[9][15].

Quellen:
[1] [PDF] Ausbildungsrahmenplan für die Berufsausbildung zum ... - IHK https://www.ihk.de/blueprint/servlet/resource/blob/1088034/131e60a061ba576d241729c8e4a93d3b/rahmenplan-fachinformatikerin-data.pdf
[2] [PDF] Sachliche und zeitliche Gliederung https://www.ihk-nuernberg.de/fileadmin/IHK_Nuernberg/Ausbildung/Berufe_A-Z_Unterlagen/Gliederung_kfm/Fachinformatiker_Systemintegration_2023.pdf
[3] Kubernetes und Docker im Vergleich - Atlassian https://www.atlassian.com/de/microservices/microservices-architecture/kubernetes-vs-docker
[4] [PDF] Docker Handbuch für Einsteiger - BMU Verlag https://bmu-verlag.de/reading-sample/?book=czoyOiIyMCI7&prop=czoyOiI2MSI7&amp=
[5] Kubernetes. Das Praxisbuch für Entwickler und DevOps-Teams https://www.rheinwerk-verlag.de/kubernetes-das-praxisbuch-fuer-entwickler-und-devops-teams/
[6] Der Containerdienst und seine Aufgabenfelder https://primegenenergycorp.com/2022/09/20/der-containerdienst-und-seine-aufgabenfelder/
[7] Kubernetes: Eine Einführung in 120 Minuten // deutsch - YouTube https://www.youtube.com/watch?v=1SaPfm96lY4
[8] Docker für Einsteiger: Ein praktischer Leitfaden zu Containern https://www.datacamp.com/de/tutorial/docker-tutorial
[9] Lernfeld 12b - Kundenspezifische Systemintegration (FISI) https://www.techbeck.com/lernfeld-12b-kundenspezifische-systemintegration-fisi/
[10] [PDF] Rahmenlehrplan für die Ausbildungsberufe - KMK https://www.kmk.org/fileadmin/Dateien/pdf/Bildung/BeruflicheBildung/rlp/Fachinformatiker_19-12-13_EL.pdf
[11] Docker. Praxisbuch für Entwickler und DevOps-Teams https://www.rheinwerk-verlag.de/docker-das-praxisbuch-fuer-entwickler-und-devops-teams/
[12] Theoretische Grundlagen | DVA Praktikum https://tha.de/~knolljo/dva/1_docker/2_grundlagen/
[13] [PDF] Fachinformatiker Fachinformatikerin Ausbildungsrahmenplan - IHK https://www.ihk.de/blueprint/servlet/resource/blob/4846792/738d26debf809e2058ed33109561ccff/rahmenplan-fachinformatiker-in-2020-data.pdf
[14] Skill up with Docker Training https://www.docker.com/trainings/
[15] Fachinformatiker/ -in Fachrichtung Systemintegration https://www.bibb.de/dienst/berufesuche/profile/apprenticeship/olkiu98
[16] Docker Fundamentals Training Material - GitHub https://github.com/nbrownuk/docker-fundamentals
[17] Verordnung über die Berufsausbildung zum Fachinformatiker und ... https://www.gesetze-im-internet.de/fiausbv/BJNR025000020.html
[18] Docker Handbuch für Einsteiger: Der leichte Weg zum ... - AZ-Delivery https://www.az-delivery.de/products/docker-handbuch-fur-einsteiger-der-leichte-weg-zum-docker-experten
[19] Ausbildungsplan Fachinformatiker Systemintegration https://it-abschlusspruefung.de/news-blog/ausbildungsplan-fachinformatiker-systemintegration
[20] [PDF] Fachinformatiker / Fachinformatikerin - Fachrichtung Systemintegration https://www.ihk.de/blueprint/servlet/resource/blob/5025526/b7174eaa6d203c13be051f01194aec95/rahmenplan-fachinformatiker-systemintegration-data.pdf
[21] Kubernetes und Docker im Vergleich | CrowdStrike https://www.crowdstrike.com/de-de/cybersecurity-101/cloud-security/kubernetes-vs-docker/
[22] Docker & Kubernetes Training (Basis) - cloudpunks GmbH https://www.cloudpunks.de/loesungen/cloud-training-workshops/kubernetes-basis-training/
[23] Martin Helmich über Docker und Kubernetes - IT-Berufe-Podcast https://it-berufe-podcast.de/martin-helmich-ueber-docker-und-kubernetes-anwendungsentwickler-podcast-121/
[24] Praxis-Workshop für Docker und Kubernetes: Der komplette Einstieg https://www.gfu.net/seminare-schulungen-kurse/open_source_sk62/docker-kubernetes-praxis-workshop-einstieg_s2109.html
[25] Docker & Kubernetes Intensiv-Schulung - workshops.de https://workshops.de/seminare-schulungen-kurse/docker-kubernetes
[26] Downloadbereich Rahmenlehrpläne - KMK https://www.kmk.org/themen/berufliche-schulen/duale-berufsausbildung/downloadbereich-rahmenlehrplaene.html
[27] Docker-Tutorial: Einführung zur beliebten Container-Plattform - IONOS https://www.ionos.de/digitalguide/server/konfiguration/docker-tutorial-installation-und-erste-schritte/
[28] Docker - Practical Guide for Developers and DevOps Teams https://www.rheinwerk-verlag.de/docker-practical-guide-for-developers-and-devops-teams/
[29] Containerisierung: Docker, Grundlagen, Praxis | StudySmarter https://www.studysmarter.de/schule/informatik/programmiersprachen/containerisierung/
[30] Docker Grundlagen - CCD Akademie https://ccd-akademie.de/docker-grundlagen/
[31] Docker Praxiseinstieg, 2. Auflage 2020 +++ Neu & direkt vom Verlag ... https://www.ebay.de/itm/184242980254
[32] Abschlussprojekt Docker - Fachinformatiker.de https://www.fachinformatiker.de/topic/157038-abschlussprojekt-docker/
[33] Der Kubernetes-Kurs für Entwickler und DevOps - Rheinwerk Verlag https://www.rheinwerk-verlag.de/seminare/kubernetes-devops/
[34] Container Technologie: Docker und Kubernetes - Grundlagen https://www.it-schulungen.com/seminare/netzwerktechnologien/kubernetes/container-technologie-docker-und-kubernetes.html
[35] Kurs: Container-Orchestrierung mit Docker und Kubernetes | skill it https://www.haufe-akademie.de/skill-it/products/36190
[36] Docker und Kubernetes für Cloud-native Softwareentwicklung https://heise-academy.de/Workshops/docker-kubernetes
[37] Kubernetes und Docker Training mit Thinkport https://thinkport.digital/docker-und-kubernetes-lernen/
[38] Microservices mit Docker und Kubernetes - IT-Schulungen.com https://www.it-schulungen.com/seminare/softwareentwicklung/softwaredesign-und-softwarearchitekturen/microservices/microservices-mit-docker-und-kubernetes.html
[39] Einführung in Docker und Kubernetes für Java Entwickler https://www.qualiero.com/lerninhalte/classroom-trainings/einfuehrung-in-docker-und-kubernetes-fuer-java-entwickler.html
[40] Was ist Container-Orchestrierung? - Red Hat https://www.redhat.com/de/topics/containers/what-is-container-orchestration
[41] [PDF] ITKwebcollege.ADMIN ITKservice https://www.itkservice.net/dokumente/136/140618145830ITKwebcollege_ADMIN_Ausbildungsinhalte.pdf
[42] Kubernetes Schulung | Container-Orchestrierung Lernen - netways https://netways.de/schulungen/kubernetes/
[43] Seminar: Deep Dive Docker Compose & Kubernetes - crowdcode.io https://www.crowdcode.io/seminare/docker-compose-kubernetes
[44] Lernfeld 12b - Fachrichtung Systemintegration https://www.schule-bw.de/faecher-und-schularten/berufliche-schularten/berufsschule/lernfelder/etechnik/fachinformatik/lf12b
[45] [PDF] Bildungsplan Fachinformatikerin/Fachinformatiker https://www.berufsbildung.nrw.de/cms/upload/_lehrplaene/a/fachinformatiker.pdf
[46] [PDF] Übersicht über die Lernfelder für den Ausbildungsberuf https://kstl.de/wp-content/uploads/2020/04/Lernfelder-FI-Systemintegration.pdf
[47] Docker & Kubernetes für Spring-Boot-Entwickler: virtueller Drei ... https://karrierewelt.golem.de/products/docker-kubernetes-fur-spring-boot-entwickler-virtueller-drei-tage-workshop
[48] Docker Praxis-Challenges: Praktisches Lernen für die Beherrschung ... https://labex.io/de/courses/docker-practice-challenges
[49] Übersicht Lernfelder 10b 11b 12b IT-Projekt Systemintegration http://www.fachinformatiker.schule/doku.php?id=uebersicht_lernfelder_10b_11b_12b_it_projekt_systemintegration
[50] Kubernetes Grundkurs als Online Kurs - Schulung - Seminar - Webinar https://www.kebel.de/kubernetes-grundkurs/
[51] Docker komplett: Vom Anfänger zum Profi (inkl. Kubernetes) | Udemy https://www.udemy.com/course/docker-komplett/
[52] Kubernetes Training: Ihr Einstieg in Container | 3 Tage Schulung https://devopscon.io/camps/kubernetes-camp/
[53] Container Technologie: Docker und Kubernetes Workshop https://karrierewelt.golem.de/products/docker-und-kubernetes-theorie-praxis-workshop?_pos=25&_fid=4823f00b5&_ss=c
[54] 64-192 Projekt Einsatz von Kubernetes, Docker und Co für die ... https://www.inf.uni-hamburg.de/inst/ab/art/teaching/ws2023/proj-einsatz-von-kubernetes.html
[55] Docker & Kubernetes: The Practical Guide [2025 Edition] - Udemy https://www.udemy.com/course/docker-kubernetes-the-practical-guide/
[56] Docker und Kubernetes - Grundlagen Container-Virtualisierung https://ppedv.de/schulung/kurse/containerDockerKuberneteseinstieg
[57] Kubernetes from Basic to Advanced Schulung https://www.nobleprog.de/cc/kubernetes
[58] Projektantrag: Modernisierung einer Software - Fachinformatiker.de https://www.fachinformatiker.de/topic/172746-projektantrag-modernisierung-einer-software/
[59] Docker und Kubernetes Hands-On - Training - socreatory https://www.socreatory.com/de/trainings/docker-kubernetes
[60] [PDF] Anlage 2 Teil A zu § 11 Ausbildungsrahmenplan für ... - LANUK NRW https://www.lanuk.nrw.de/fileadmin/lanuv/Ausbildung/AUsbildungsrahmenplan_Fachinformatiker-data.pdf
[61] [PDF] Ausbildungsrahmenplan https://karriere.kbs.de/SharedDocs/Downloads/nwk/fi_systemintegration_ausbildungsrahmenplan_nbf.pdf?__blob=publicationFile
[62] [PDF] Der neue KMK-Rahmenlehrplan Technische IT-Berufe https://www.berufsbildung.nrw.de/cms/upload/fachinformatiker/tagung/3_neue_rlp_herr_mielke.pdf
[63] [PDF] Rahmenlehrplan https://karriere.kbs.de/SharedDocs/Downloads/nwk/fi_anwendungsentw_rahmenlehrplan_nbf.pdf?__blob=publicationFile

---

