Bitte schreibe mir ein ausführliches Beispiel für das Design Pattern "Adapter" - achte darauf, dass das Beispiel praktisch sinnvoll ist.

Gerne! Das Adapter-Design-Pattern ist ein strukturelles Muster, das zwei inkompatible Schnittstellen miteinander verbindet, sodass sie zusammenarbeiten können. Es ist besonders nützlich, wenn du eine Klasse verwenden möchtest, die eine bestimmte Schnittstelle erwartet, du aber eine andere Schnittstelle zur Verfügung hast.

Hier ist ein praktisches Beispiel für das Adapter-Pattern in einem Software-Entwicklungskontext:

### Szenario

Stellen wir uns vor, wir entwickeln ein Software-System für ein Unternehmen, das verschiedene Arten von Druckern verwendet. Die Anwendung muss in der Lage sein, Dokumente auf diesen Druckern auszudrucken. Es gibt jedoch zwei Haupttypen von Druckern: **AlteDrucker** und **NeueDrucker**. 

Die `AlteDrucker` haben eine Methode `druckeText(String text)`, während die `NeueDrucker` eine Methode `printDocument(Document doc)` verwenden. Unsere Anwendung hat jedoch ursprünglich nur mit den `AlteDrucker` gearbeitet und erwartet die Methode `druckeText`.

### Ziel

Wir möchten die `NeueDrucker` ohne Änderungen an der bestehenden Drucklogik verwenden.

### Lösung

Wir nutzen das Adapter-Design-Pattern, um einen Adapter zu erstellen, der zwischen unserer bestehenden Logik und den `NeueDrucker` vermittelt.

```java
// Vorhandene Schnittstelle für AlteDrucker
interface AlteDrucker {
    void druckeText(String text);
}

// Klasse für Neue Drucker
class NeueDrucker {
    public void printDocument(Document doc) {
        // Logik zum Drucken des Dokuments
        System.out.println("Neuer Drucker druckt: " + doc.getContent());
    }
}

// Dokument-Klasse (für neue Drucker)
class Document {
    private String content;

    public Document(String content) {
        this.content = content;
    }

    public String getContent() {
        return content;
    }
}

// Der Adapter: Er implementiert die Schnittstelle der alten Druckersysteme
class NeueDruckerAdapter implements AlteDrucker {
    private NeueDrucker neuerDrucker;

    public NeueDruckerAdapter(NeueDrucker neuerDrucker) {
        this.neuerDrucker = neuerDrucker;
    }

    @Override
    public void druckeText(String text) {
        // Konvertiere den Text in ein Document und verwende den neuen Druckervorgang
        Document doc = new Document(text);
        neuerDrucker.printDocument(doc);
    }
}

// Beispielanwendung
public class MainApp {
    public static void main(String[] args) {
        // Verwenden eines alten Druckers
        AlteDrucker alterPrinter = new AlterPrinter();
        alterPrinter.druckeText("Hello World!");

        // Verwenden eines neuen Druckers über den Adapter
        NeueDrucker neuerPrinter = new NeueDrucker();
        AlteDrucker adapter = new NeueDruckerAdapter(neuerPrinter);
        
        adapter.druckeText("Hello from the new printer!");
    }
}

// Implementierung eines alten Printers zur Vollständigkeit des Beispiels
class AlterPrinter implements AlteDrucker {
    @Override
    public void druckeText(String text) {
        System.out.println("Alter Druckertyp druckt: " + text);
    }
}
```

### Erklärung

1. **AlteSchnittstelle**: Die bestehende Anwendung arbeitet mit der `AlteSchnittstelle`, die die Methode `druckeText()` bereitstellt.
   
2. **NeuesSystem**: Die neuen Drucksysteme verwenden eine andere Methode (`printDocument()`), um Dokumente zu drucken.

3. **Adapter**: Der `NeueSchnittstelleAdapter` ermöglicht es uns, einen neuen Druckertyp innerhalb des bestehenden Systems zu verwenden, indem er als Vermittler zwischen den unterschiedlichen Schnittstellen agiert.

Dieses Beispiel zeigt anschaulich, wie das Adapter-Design-Pattern genutzt werden kann, um neue Komponenten in ein bereits bestehendes System zu integrieren, ohne dass große Änderungen am Gesamtsystem vorgenommen werden müssen.