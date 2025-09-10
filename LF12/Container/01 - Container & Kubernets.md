![[Pasted image 20250515085949.png]]

In diesem Vortrag erklärt Sai Benin, ein Entwickleradvokat bei IBM, die Grundlagen der Containerisierung und deren Vorteile gegenüber virtuellen Maschinen (VMs). Er beginnt mit einem Überblick über die Geschichte der Containertechnologie, die ihren Ursprung in den 2008 eingeführten Cgroups im Linux-Kernel hat. Diese Technologie bereitete den Weg für moderne Containerlösungen wie Docker, Kubernetes, Cloud Foundry und Rocket.

Benin veranschaulicht den Unterschied zwischen VMs und Containern anhand eines Node.js-Anwendungsbeispiels. Bei der Verwendung von VMs wird neben dem Host-Betriebssystem auch ein Gast-Betriebssystem benötigt, was zu einer größeren Ressourcennutzung führt. Im Gegensatz dazu benötigen Container nur die notwendigen Bibliotheken und Binärdateien ohne ein zusätzliches Betriebssystem, was sie ressourcenschonender macht.

Der Prozess der Containerisierung umfasst drei Schritte: das Erstellen eines Manifests (z.B. Dockerfile), das Bauen des Images (z.B. Docker-Image) und das Erstellen des Containers selbst. Dieser Prozess bleibt unabhängig von der verwendeten Containertechnologie gleich.

Ein weiterer Vorteil von Containern ist ihre Modularität, die eine einfachere Skalierung ermöglicht. Anwendungen können unabhängig voneinander in separaten Containern laufen, was eine bessere Ressourcennutzung und Flexibilität bietet. Dies erleichtert auch die Implementierung von Cloud-nativen Architekturen.

Abschließend hebt Benin hervor, dass Container Portabilität ermöglichen und agilere DevOps-Prozesse sowie kontinuierliche Integration und Bereitstellung unterstützen.

Ergänzungen:
1. **Cgroups und Namespaces**: Cgroups (Control Groups) und Namespaces sind zwei grundlegende Technologien im Linux-Kernel, die Containerisierung ermöglichen. Cgroups verwalten und limitieren die Ressourcennutzung (CPU, Speicher, I/O) von Prozessen, während Namespaces eine isolierte Ausführungsumgebung bieten, indem sie Systemressourcen wie Prozess-IDs, Netzwerkstacks oder Dateisysteme virtualisieren.

2. **Docker**: Docker ist eine beliebte Containerisierungsplattform, die auf den Technologien von Cgroups und Namespaces aufbaut. Es bietet ein einfaches CLI-Tool zum Erstellen, Verwalten und Ausführen von Containern. Das Dockerfile ist ein textbasiertes Skript zur Automatisierung des Image-Erstellungsprozesses, das genaue Anweisungen zur Konfiguration einer Containerumgebung enthält.

3. **Kubernetes**: Kubernetes ist eine Orchestrierungsplattform für Container-Anwendungen. Es automatisiert das Deployment, die Skalierung und den Betrieb von Container-Anwendungen in Clustern. Kubernetes verwaltet Container in Pods (die kleinste deploybare Einheit) und verwendet Services für Load Balancing sowie ConfigMaps und Secrets für die Konfiguration.

4. **Container Image Layers**: Ein Docker-Image besteht aus mehreren read-only Schichten (Layers). Jede Schicht repräsentiert einen Zwischenzustand des Images nach dem Ausführen eines Befehls im Dockerfile. Diese Layer-Struktur erhöht die Effizienz durch Wiederverwendung bereits existierender Schichten bei der Erstellung neuer Images.

5. **Security Aspects**: Während Container eine Isolation zwischen Anwendungen bieten können, teilen sie sich denselben Kernel des Host-Betriebssystems, was potenzielle Sicherheitsrisiken birgt. Sicherheitsmaßnahmen umfassen das Verwenden minimaler Basisimages (z.B., Alpine Linux), das regelmäßige Aktualisieren von Images sowie das Einsetzen von Tools wie SELinux oder AppArmor zur weiteren Isolierung.

6. **Networking in Containers**: Container-Netzwerke ermöglichen die Kommunikation zwischen Containers sowie externen Systemen über verschiedene Netzwerkmodi wie Bridge-, Host- oder Overlay-Netzwerke in Docker.

7. **Persistent Storage**: Da Container oft kurzlebig sind und keine Daten über Neustarts hinaus speichern sollen, wird persistenter Speicher durch Volumes oder Bind-Mounts bereitgestellt. Diese ermöglichen es Containern, Daten dauerhaft zu speichern oder bestehende Daten aus dem Host-System zu integrieren.

Diese technischen Details bieten einen tieferen Einblick in die Funktionsweise der Containerisierungstechnologie und deren Anwendungen in modernen IT-Infrastrukturen.

---
weiteres Material: https://www.youtube.com/watch?v=O5LEvNCIUHU

## Unterschied Docker & Kubernetes:
https://www.atlassian.com/de/microservices/microservices-architecture/kubernetes-vs-docker
