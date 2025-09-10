## ✅ **Beispielcode für Aufgabe 1: Müllsammel-Roboter**

### 📌 Klassenübersicht:

``` java

class Position {
    double x, y, z;
    // Getter und Setter werden vorausgesetzt
}

class RouteCalculator {
    public static double getDistance(Position p1, Position p2) {
        // Euklidische Distanz
        double dx = p1.getX() - p2.getX();
        double dy = p1.getY() - p2.getY();
        double dz = p1.getZ() - p2.getZ();
        return Math.sqrt(dx*dx + dy*dy + dz*dz);
    }
}
```

### 📌 Algorithmus zur Berechnung der Reinigungsroute:

```java
Position[] calculateCleaningRoute(Position[] containerPositions) {
    ArrayList<Position> route = new ArrayList<>();
    ArrayList<Position> remaining = new ArrayList<>(Arrays.asList(containerPositions));

    // Start bei erster Position
    Position current = remaining.remove(0);
    route.add(current);

    while (!remaining.isEmpty()) {
        double minDistance = Double.MAX_VALUE;
        Position next = null;

        for (Position p : remaining) {
            double distance = RouteCalculator.getDistance(current, p);
            if (distance < minDistance) {
                minDistance = distance;
                next = p;
            }
        }

        route.add(next);
        remaining.remove(next);
        current = next;
    }

    return route.toArray(new Position[0]);
}
```

---

## ✅ **Beispielcode für Aufgabe 2: Medikamentenlieferung**

### 📌 Klassenübersicht:

```java
class DeliveryPoint {
    double latitude;
    double longitude;
    // Getter/Setter vorausgesetzt
}

class DistanceUtil {
    public static double calculateDistance(DeliveryPoint a, DeliveryPoint b) {
        double dLat = a.getLatitude() - b.getLatitude();
        double dLon = a.getLongitude() - b.getLongitude();
        return Math.sqrt(dLat*dLat + dLon*dLon); // Vereinfachte Distanz
    }
}

```

### 📌 Optimierungsalgorithmus:

```java
DeliveryPoint[] optimizeDeliveryRoute(DeliveryPoint[] deliveryStations) {
    ArrayList<DeliveryPoint> route = new ArrayList<>();
    ArrayList<DeliveryPoint> remaining = new ArrayList<>(Arrays.asList(deliveryStations));

    DeliveryPoint current = remaining.remove(0); // Startpunkt
    route.add(current);

    while (!remaining.isEmpty()) {
        double shortest = Double.MAX_VALUE;
        DeliveryPoint nearest = null;

        for (DeliveryPoint p : remaining) {
            double dist = DistanceUtil.calculateDistance(current, p);
            if (dist < shortest) {
                shortest = dist;
                nearest = p;
            }
        }

        route.add(nearest);
        remaining.remove(nearest);
        current = nearest;
    }

    return route.toArray(new DeliveryPoint[0]);
}
```


---

### ✨ Didaktischer Hinweis:

Beide Lösungen implementieren eine einfache **Greedy-Strategie**, bei der in jedem Schritt die **lokal optimale Entscheidung** getroffen wird. Dies lässt sich gut im Unterricht besprechen – auch hinsichtlich der Frage, ob die globale Optimierung damit immer erreicht wird.

Möchtest du noch eine **Visualisierung der Route**, eine **Testsituation** oder eine **Variation mit Gewichtung oder Einschränkungen (z. B. Höhenunterschied, Wetterdaten)**?