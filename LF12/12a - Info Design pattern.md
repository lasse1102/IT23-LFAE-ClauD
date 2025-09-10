**Unterrichtseinheit: Design Patterns in der Software-Entwicklung**

**Lernziele:**
1. Verständnis der grundlegenden Konzepte von Design Patterns.
2. Fähigkeit, die Vorteile und Anwendungsbereiche von Design Patterns zu erklären.
3. Erkennen und Implementieren ausgewählter Design Patterns in eigenen Projekten.
4. Förderung eigenständiger Recherchefähigkeiten.
### **Einführung in Design Patterns**

**Inhalt:**
- **Definition und Geschichte:**
  - Was sind Design Patterns?
  - Ursprung und Evolution der Design Patterns (Erwähnung von "Gang of Four").
  
- **Bedeutung und Vorteile:**
  - Warum sind Design Patterns wichtig?
  - Vorteile bei der Verwendung von Design Patterns in der Software-Entwicklung.

- **Kategorisierung:**
  - Kurze Übersicht über die drei Hauptkategorien von Design Patterns:
    - Erzeugungsmuster (Creational)
    - Strukturmuster (Structural)
    - Verhaltensmuster (Behavioral)
---
**Infomaterial zu Design Patterns**

**Einleitung:**
Design Patterns helfen uns, **wiederkehrende Probleme** in der Softwarearchitektur effektiv zu lösen. 
In dieser Einheit geht es darum, die Definition, Geschichte, Bedeutung und Kategorisierung dieser Patterns zu erkunden.

**Definition und Geschichte:**

- **Was sind Design Patterns?**
  Design Patterns sind bewährte Lösungsansätze für häufig auftretende Probleme in der Softwareentwicklung. Sie bieten eine **standardisierte Vorgehensweise**, um komplexe Entwurfsprobleme zu lösen und fördern so die Wiederverwendbarkeit und Wartbarkeit des Codes. Ein Design Pattern ist **keine fertige Lösung, sondern ein Vorlagenentwurf**, der je nach Bedarf angepasst werden kann.

- **Ursprung und Evolution der Design Patterns:**
  Der Begriff "Design Pattern" wurde durch das Buch "Design Patterns: Elements of Reusable Object-Oriented Software" von Erich Gamma, Richard Helm, Ralph Johnson und John Vlissides popularisiert. Dieses Werk aus dem Jahr 1994 ist gemeinhin als das "Gang of Four"-Buch bekannt. Die Autoren beschrieben darin **23 grundlegende Muster für objektorientierte Softwareentwicklung**. Seitdem haben sich Design Patterns kontinuierlich weiterentwickelt und wurden um viele weitere ergänzt.

**Bedeutung und Vorteile:**

- **Warum sind Design Patterns wichtig?**
  In der Softwareentwicklung treten oft ähnliche Probleme auf. Design Patterns bieten Ansätze für Lösungen für diese Probleme und fördern dadurch effizientes Arbeiten. Sie helfen Entwicklern dabei, klare Strukturen zu schaffen und Missverständnisse im Team zu vermeiden.

- **Vorteile bei der Verwendung von Design Patterns in der Software-Entwicklung:**
  - **Wiederverwendbarkeit:** Einmal entwickelte Lösungen können leicht auf ähnliche Probleme angewendet werden.
  - **Wartbarkeit:** Gut strukturierte Codebasen sind einfacher zu verstehen und zu pflegen.
  - **Kommunikation:** Sie schaffen eine gemeinsame Sprache innerhalb eines Entwicklerteams.
  - **Effizienz:** Durch erprobte Lösungen sparen Entwickler Zeit bei Entwurf und Implementierung.

**Kategorisierung:**

Design Patterns lassen sich grob in **drei Hauptkategorien** unterteilen:

1. **Erzeugungsmuster (Creational):**
   Diese Muster befassen sich mit der Art und Weise, wie Objekte erstellt werden. Sie abstrahieren den Instanziierungsprozess, um Flexibilität beim Erstellen neuer Objekte zu ermöglichen.
   - Beispiele: Singleton, Factory Method, Abstract Factory

2. **Strukturmuster (Structural):**
   Diese Muster beschäftigen sich mit dem Aufbau von Klassenstrukturen oder Objektkompositionen zur Schaffung neuer Funktionalitäten.
   - Beispiele: Adapter, Decorator, Composite

3. **Verhaltensmuster (Behavioral):**
   Verhaltensmuster konzentrieren sich auf die Kommunikation zwischen Objekten sowie auf deren Interaktionsverhalten.
   - Beispiele: Observer, Strategy, Command
### Vertiefung durch Beispiele

**Inhalt:**
- **Vorstellung ausgewählter Muster:**
  - Singleton (Erzeugungsmuster)
    - Konzept, Vor- und Nachteile, Beispielimplementierung
  - Adapter (Strukturmuster)
    - Konzept, Vor- und Nachteile, Beispielimplementierung
  - Observer (Verhaltensmuster)
    - Konzept, Vor- und Nachteile, Beispielimplementierung

### Singleton (Erzeugungsmuster)

**Konzept:**
Das Singleton-Pattern stellt sicher, dass eine Klasse nur eine einzige Instanz hat und bietet einen globalen Zugriffspunkt auf diese Instanz. Es wird häufig verwendet, wenn genau ein Objekt benötigt wird, um Aktionen zu koordinieren.

**Vorteile:**
- Kontrollierter Zugriff auf die einzige Instanz.
- Reduzierter Speicherverbrauch durch Vermeidung mehrerer Instanzen.
- Möglichkeit zur leicht modifizierbaren Steuerung des Lebenszyklus der Instanz.

**Nachteile:**
- Kann zu Problemen bei paralleler Programmierung führen.
- Erschwert das Testen (z.B. Unit Tests), da es schwierig ist, den Zustand des Singletons zurückzusetzen.
- Kann die Abhängigkeiten zwischen Klassen erhöhen.

**Beispielimplementierung in Python:**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Anwendung
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Ausgabe: True
```

**Anwendungsfall:**
Ein häufiges Beispiel für einen Singleton ist ein Logger in einer Anwendung. Es wird sichergestellt, dass alle Log-Einträge zentralisiert und konsistent sind.

### Adapter (Strukturmuster)

**Konzept:**
Das Adapter-Pattern ermöglicht die Zusammenarbeit von Klassen mit inkompatiblen Schnittstellen. Es dient als Brücke zwischen zwei unterschiedlichen Schnittstellen und ermöglicht so deren Interaktion.

**Vorteile:**
- Ermöglicht die Wiederverwendung vorhandener Klassen ohne Änderung ihres Codes.
- Erleichtert die Integration von Komponenten mit unterschiedlichen Schnittstellen.

**Nachteile:**
- Kann die Komplexität erhöhen durch zusätzliche Abstraktionsebenen.
- Im großen Maßstab kann es zu einer unübersichtlichen Struktur führen.

**Beispielimplementierung in Python:**

```python
class EuropeanSocket:
    def voltage(self):
        return "230V"

class USASocket:
    def voltage(self):
        return "120V"

class SocketAdapter:
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        if isinstance(self.socket, EuropeanSocket):
            return "120V"  # Anpassung der Spannung
        return self.socket.voltage()

# Anwendung
euro_socket = EuropeanSocket()
adapter = SocketAdapter(euro_socket)

print(adapter.voltage())  # Ausgabe: 120V
```

**Anwendungsfall:**
Adapter werden häufig verwendet, um Softwarekomponenten mit unterschiedlichen APIs miteinander kommunizieren zu lassen. Ein Beispiel wäre das Anpassen eines bestehenden Systems an eine neue Datenbank-Schnittstelle.

### Observer (Verhaltensmuster)

**Konzept:**
Das Observer-Pattern definiert eine Eins-Zu-Viele-Abhängigkeit zwischen Objekten. Wenn ein Objekt seinen Zustand ändert, werden alle abhängigen Objekte benachrichtigt und automatisch aktualisiert.
**Vorteile:**
- Fördert lose Kopplung zwischen dem Subjekt und den Beobachtern.
- Erleichtert die dynamische Änderung der Beobachterliste zur Laufzeit.

**Nachteile:**
- Benachrichtigungen können unerwartet auftreten oder schwer nachzuverfolgen sein.
- Bei vielen Beobachtern kann es zu Leistungsproblemen kommen.

**Beispielimplementierung in Python:**

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

# Konkreter Beobachter
class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"{self} beobachtet {subject}")

# Anwendung
subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)
subject.notify()  # Beide Beobachter werden
```

---
**Aktivität:**
- **Gruppenarbeit:** Wählt jeweils ein anderes Muster aus den oben genannten Kategorien aus und stellt es in einem Schaubild zur Erklärung des Musters kurz vor. 
### Praktische Anwendung

**Inhalt & Aktivitäten:** 
1. **Präsentationen aus der Gruppenarbeit:** 
   Jeder präsentiert das gewählte Muster inklusive eines konkreten Code-Beispiels.

2. **Hands-On Übung:** 
   Implementiert ein einfaches Projekt, das mindestens zwei verschiedene Muster verwendet. Zum Beispiel könnte dies eine einfache Chat-Anwendung sein, die das Singleton-Muster für die Instanzverwaltung des Chat-Managers nutzt und das Observer-Muster für Benachrichtigungen bei neuen Nachrichten.

3. **Reflexion & Diskussion:** 
   Besprecht untereinander:
   - Welche Herausforderungen sind bei der Implementierung aufgetreten?
   - Wie haben die verwendeten Muster den Entwicklungsprozess unterstützt?

---

**Abschluss & Evaluation:**

- Kurze Umfrage oder Feedback-Runde:
  "Wie hilfreich waren diese Muster für euer Verständnis beim Lösen typischer Probleme?"