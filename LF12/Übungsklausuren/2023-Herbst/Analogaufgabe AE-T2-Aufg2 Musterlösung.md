---
{}
---
### Musterlösung (Pseudocode)

```java
DeliveryLocation[] planRoute(DeliveryLocation[] deliveryLocations) {
    DeliveryLocation[] route = new DeliveryLocation[deliveryLocations.length]; // Array für die Route
    route[0] = deliveryLocations[0]; // Position 0 als Startadresse
    DeliveryLocation currentLocation = deliveryLocations[0]; // Setze die aktuelle Position auf die Startadresse
    deliveryLocations.remove(0); // Entferne die Startadresse aus dem Array der noch anzufahrenden Adressen

    while (deliveryLocations.length > 0) { // Solange noch Adressen vorhanden sind
        double minDistance = Double.MAX_VALUE; // Initialisiere die minimale Distanz
        int closestIndex = -1; // Index der nächsten Adresse

        // Durchlaufe alle verbleibenden Adressen
        for (int i = 0; i < deliveryLocations.length; i++) {
            double distance = DistanceCalculator.calculateDistance(currentLocation, deliveryLocations[i]); // Berechne die Distanz
            if (distance < minDistance) { // Wenn die gefundene Distanz kleiner ist als die minimale Distanz
                minDistance = distance; // Update die minimale Distanz
                closestIndex = i; // Update den Index der nächsten Adresse
            }
        }

        // Speichere die nächstgelegene Adresse im route Array
        route[route.length - deliveryLocations.length] = deliveryLocations[closestIndex];
        currentLocation = deliveryLocations[closestIndex]; // Setze die aktuelle Position auf die nächstgelegene Adresse
        deliveryLocations.remove(closestIndex); // Entferne die nächstgelegene Adresse aus dem Array
    }

    return route; // Gebe das Array der geplanten Route zurück
}
```

### Erklärung der Musterlösung:

- Der Algorithmus beginnt mit der Initialisierung des `route` Arrays und setzt die erste Adresse auf die Startadresse.
- Die Schleife läuft, solange es noch Adressen im `deliveryLocations` Array gibt.
- Innerhalb der Schleife wird für jede verbleibende Adresse die Entfernung zur aktuellen Position berechnet und die Adresse mit der kürzesten Distanz wird ausgewählt.
- Diese Adresse wird dann im `route` Array gespeichert, als neue aktuelle Position gesetzt und aus dem `deliveryLocations` Array entfernt.
- Am Ende wird das `route` Array zurückgegeben, das die Reihenfolge der angefahrenen Adressen enthält.