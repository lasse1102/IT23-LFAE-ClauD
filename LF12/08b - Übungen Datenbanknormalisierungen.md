### Aufgabe 1: Einführung in die Normalisierung
**Ziel:** Verstehen der Grundlagen der Datenbanknormalisierung.

- Erkläre die Begriffe: Erste Normalform (1NF), Zweite Normalform (2NF) und Dritte Normalform (3NF).
	- *1NF: Jede Zeile steht für sich atomar, Bsp.: Adresse muss in PLZ, Ort, Straße aufgeschlüsselt werden*
	- *2NF: Keine Abhängigkeiten, außer der von den Schlüsselattributen -> Alle Nicht-Schlüsselattribute müssen vollständig von einem Primärschlüssel abhängen.*
	- *3NF: Kein Nicht-Schlüsselattribut darf von einem Nicht-Schlüsselattribut abhängen. Bsp.: PLZ und Ort werden zusammen erfasst, aber aus der PLZ lässt sich der Ort eindeutig ermitteln.*
- Warum ist es wichtig, eine Datenbank zu normalisieren? Nenne mindestens drei Vorteile.
	1. *Speicherplatz sparen* (auch durch Vermeidung von Redundanzen)
	2. *Verhindert Anomalien -> Datenintegrität / -konsistenz (wichtig z. B. bei Löschvorgängen)*
	3. *Wartung der Datenbank wird erleichtert -> Reduzierung von Redundanzen*
	4. *Performanz der Datenbank wird potentiell erhöht (z. B. große, datenintensive Datenbanken -> gespeicherte Bilder müssten erst abgerufen werden, um Metadaten auszulesen)*
	5. *Skalierbarkeit ist höher*
- Welche Probleme können auftreten, wenn eine Datenbank nicht normalisiert ist?
	- *Löschanomalien -> Kollateralschäden beim Löschen von Daten (Inkonsistenzen)*
	- *schlechtere Performanz, geringere Wartbarkeit usw. -> siehe Punkt 2 negiert* 
	- *Extrahieren / Löschen von Daten ist schwieriger und generiert Probleme --> Schnittstellenprobleme*

### Aufgabe 2: Anwendung der Ersten Normalform
**Ziel:** Umsetzung der 1NF in einer vorgegebenen Tabelle.

- Gegeben ist eine Tabelle mit den Spalten: `Bestellnummer`, `Kunde`, `Artikel1`, `Artikel2`, `Artikel3`.
- Bringe diese Tabelle in die Erste Normalform. Erkläre deine Schritte.
#### Lösung
* *'Kunde' aufschlüsseln* -> Name, Adresse ,....
* *Artikel1, Artikel2, ...* -> Artikel

	Bestellnummer | Kunde | Artikel
	--------------------------------
	1001          | Schmidt | Artikel A
	1001          | Schmidt | Artikel B
	1001          | Schmidt | Artikel C
### Aufgabe 3: Übergang zur Zweiten Normalform
**Ziel:** Umwandlung einer Tabelle von 1NF in 2NF.

- Betrachte die folgende Tabelle in 1NF:
  ```
  Bestellnummer | Kunde | ArtikelID | ArtikelName | Menge | KundenAdresse
  ```
- Identifiziere mögliche funktionale Abhängigkeiten.
- Bringe die Tabelle in die Zweite Normalform. Beschreibe den Prozess und begründe deine Entscheidungen.

#### Lösung
* *ArtikelName ist von ArtikelID abhängig und nicht von Bestellnummer* -> in separate Tabelle auslagern und über Verbindung von Primär- und Fremdschlüssel
* *Aufteilung in drei Tabellen: Kundendaten: KundenID, Kunde, KundenAdresse*
						 *Bestelldaten: Bestellnummer, KundenID, ArtikelID, Menge*
						 *Artikel: ArtikelID, ArtikelName*

##### Andere Beispielaufteilung
Tabelle Bestellungen:
```
Bestellnummer | Kunde | KundenAdresse
--------------------------------------
1001          | Müller   | Straße A 
```

Tabelle Bestellpositionen:
```
Bestellnummer | ArtikelID | Menge
---------------------------------
1001          | A123      | 10   
```

Tabelle Artikel:
```
ArtikelID     | ArtikelName 
---------------------------
A123          | Stuhl      
```
### Aufgabe 4: Dritte Normalform erreichen
**Ziel:** Anwendung der 3NF auf eine bestehende Datenstruktur.

- Eine Tabelle sieht wie folgt aus:
  ```
  ArtikelID | ArtikelName | LieferantID | LieferantName | LieferantAdresse
  ```
- Welche funktionalen Abhängigkeiten existieren hier?
- Bringe diese Struktur in die Dritte Normalform und erläutere den Prozess.

#### Lösung
Tabelle Lieferanten:
LieferantID | LieferantName | LieferantAdresse

Tabelle Artikel:
ArtikelID | ArtikelName

(Zwischen-)Tabelle Lieferung:
LieferantID | ArtikelID


---
## Praktische Aufgaben
### Aufgabe 5: Analyse eines bestehenden Systems
**Ziel:** Bewertung einer realen oder fiktiven Datenbank bezüglich ihrer Normalformen.

- Wähle ein kleines bestehendes Datenbanksystem aus (z.B., ein einfaches Shop-System).
- Analysiere es hinsichtlich seiner aktuellen Normalisierungsstufe.
- Schlage Verbesserungen vor, um mindestens die Dritte Normalform zu erreichen. Diskutiere mögliche Vor- und Nachteile dieser Änderungen.

### Aufgabe 6: Praktische Implementierung
**Ziel:** Umsetzung des Gelernten in einem praktischen Projekt.

- Erstelle ein kleines Datenbankschema für ein Bibliothekssystem, das folgende Anforderungen erfüllt:
    - Verwaltung von Büchern mit Titel, Autor(en), ISBN und Genre.
    - Verwaltung von Mitgliedern mit Namen, Adresse und Telefonnummer.
    - Möglichkeit zur Ausleihe von Büchern durch Mitglieder mit Datum der Ausleihe und Rückgabedatum.
  
Bringe dein Schema mindestens bis zur Dritten Normalform. Dokumentiere alle Schritte der Normalisierung inklusive der Begründung für jede Transformation.
