## ✅ **Alternative Aufgabe 1: Müllsammel-Roboter auf einem Betriebsgelände**

### **Ausgangssituation:**

Die Firma CleanBot Systems GmbH entwickelt autonome Reinigungsroboter für große Betriebsgelände. Die Roboter sollen Müllcontainer nacheinander anfahren, wobei sie stets den jeweils **nächstgelegenen Container** ansteuern sollen.

### **Gegeben:**

Die Positionen der Müllcontainer liegen in einem Array `containerPositions` als Objekte der Klasse `Position` vor:

``` java
class Position {   double x;   double y;   double z; }
```

```Die Methode zur Berechnung der Entfernung zwischen zwei Positionen ist in der Klasse `RouteCalculator` bereits vorhanden:

```java
class RouteCalculator {   public static double getDistance(Position p1, Position p2) }
```

### **Aufgabenstellung:**

Entwickeln Sie einen Algorithmus `calculateCleaningRoute()`, der das Ergebnis in einem Array `cleaningRoute` speichert. Die Route beginnt immer bei `containerPositions[0]` (Startpunkt). Die Arbeitsweise des Algorithmus soll wie folgt sein:

- Die Position `containerPositions[0]` wird als Startpunkt in `cleaningRoute` gespeichert und aus `containerPositions` entfernt.
    
- Solange Positionen vorhanden sind:
    
    - Ermittle die Position mit der **kürzesten Entfernung** zur aktuellen Position.
        
    - Füge diese zur `cleaningRoute` hinzu und entferne sie aus `containerPositions`.
        
    - Setze diese Position als neue aktuelle Position.
        

**Tipp:** Der größte Doublewert ist über `Double.MAX_VALUE` abrufbar.

**Erstellen Sie den vollständigen Pseudocode für den beschriebenen Algorithmus.**

---

## ✅ **Alternative Aufgabe 2: Medikamentenlieferung mit Lieferdrohne im Krankenhausgelände**

### **Ausgangssituation:**

Die MediDrone AG plant ein Drohnensystem für die Lieferung von Medikamenten innerhalb eines großen Krankenhausgeländes. Die Drohne startet am Hauptlager (erste Position im Array) und soll die Medikamentenstationen in der effizientesten Reihenfolge anfliegen – jeweils die Station, die am nächsten zur aktuellen Position liegt.

### **Gegeben:**

Die Positionen der Stationen sind als Array `deliveryStations` mit Objekten der Klasse `DeliveryPoint` gespeichert:

```java
class DeliveryPoint {   double latitude;   double longitude; }
```

Die Entfernungsberechnung erfolgt mit:

``` java
class DistanceUtil {   public static double calculateDistance(DeliveryPoint a, DeliveryPoint b) }
```

### **Aufgabenstellung:**

Erstellen Sie den Algorithmus `optimizeDeliveryRoute()`, der eine optimierte Route in einem Array `optimizedRoute` zurückgibt. Dabei gilt:

- Start ist immer `deliveryStations[0]`.
    
- Die Route enthält alle Stationen in der Reihenfolge, in der sie von der Drohne angeflogen werden sollen.
    
- Die jeweils **nächstgelegene** Station zur aktuellen Position wird als Nächstes angeflogen.
    

**Hinweise:**

- Der Algorithmus darf das Ursprungsarray `deliveryStations` verändern.
    
- Die aktuelle Position wird nach jedem Schritt aktualisiert.
    

**Erstellen Sie den vollständigen Pseudocode.**