## ✅ **Aufgabe 1: Reifegradbestimmung von Bananen mit Farbsensor**

### **Ausgangssituation:**

Die TropiSoft GmbH entwickelt Softwarelösungen für Plantagen in tropischen Gebieten. Ein neues System soll die Reife von Bananen anhand ihrer Schalenfarbe und Umgebungstemperatur bestimmen, um die optimale Erntezeit zu prognostizieren.

### **Aufgabenstellung:**

Eine App soll entwickelt werden, die nach dem Start folgende Schritte ausführt:

1. Die Farbe der Bananenschale wird von einem Farbsensor analysiert und über die Methode `einlesenFarbe()` der Klasse `GUI` eingelesen.
    
2. Falls die Farbe als "grün" erkannt wird, erfolgt keine weitere Messung.
    
    - Es erfolgt die Ausgabe: „Bananen sind noch unreif“ (über die Methode `ausgabe(...)` der Klasse `GUI`).
        
3. Ist die Farbe „gelb“ oder „braun“, wird zusätzlich die Umgebungstemperatur abgefragt (`einlesenTemperatur()`).
    
4. Die Methode `berechneReifestufe(farbe, temperatur)` der Klasse `Reifeanalysator` berechnet die Reifestufe.
    
5. Die Ausgabe erfolgt je nach Ergebnis:
    
    - Reifestufe = 3: „Ernte optimal“
        
    - Reifestufe = 2: „Ernte bald möglich“
        
    - Reifestufe = 1: „Bananen überreif – schnell ernten“
        

**Erstellen Sie ein Sequenzdiagramm, das den beschriebenen Ablauf darstellt.**

---

## ✅ **Aufgabe 2: Luftqualitätsanalyse in Innenräumen**

### **Ausgangssituation:**

Die Firma AirSense IT Solutions entwickelt Apps zur Analyse von Raumluftqualität in Smart Buildings. Eine App soll CO₂- und Feinstaubwerte einlesen, um Empfehlungen für das Raumklima zu geben.

### **Aufgabenstellung:**

Nach dem Start der App erfolgt eine Messung des CO₂-Werts durch die Methode `einlesenCO2()` der Klasse `SensorGUI`.

1. Falls der CO₂-Wert über 1500 ppm liegt:
    
    - Ausgabe: „Lüften dringend erforderlich“ (`ausgabe(...)` der Klasse `SensorGUI`)
        
    - Weitere Messungen entfallen.
        
2. Falls der CO₂-Wert ≤ 1500 ppm:
    
    - Der Feinstaubwert wird gemessen über `einlesenFeinstaub()` der Klasse `SensorGUI`.
        
    - Die Methode `analysiereLuftqualität(co2, feinstaub)` der Klasse `Luftanalysator` bestimmt die Luftqualität.
        
    - Die Qualität wird in drei Stufen klassifiziert:
        
        - **Stufe 1:** „Luftqualität sehr gut“
            
        - **Stufe 2:** „Luftqualität akzeptabel“
            
        - **Stufe 3:** „Luftqualität schlecht“
            

**Erstellen Sie ein Sequenzdiagramm, das den beschriebenen Ablauf der App abbildet.**