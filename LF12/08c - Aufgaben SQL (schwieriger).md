### Aufgabe 1: Kunden- und Bestelldatenbank

**Beschreibung:** Gegeben sind zwei Tabellen: `Kunden` und `Bestellungen`.

- Tabelle `Kunden`: 
  - `kunde_id` (Primary Key)
  - `name`
  - `stadt`

- Tabelle `Bestellungen`: 
  - `bestellung_id` (Primary Key)
  - `kunde_id` (Foreign Key)
  - `betrag`
  - `datum`

**Aufgabe:** Schreibe eine SQL-Abfrage, die den Namen der Kunden, die in "Berlin" wohnen, sowie den Durchschnittsbetrag ihrer Bestellungen anzeigt.
#### **Musterlösung:**

```sql
SELECT k.name, AVG(b.betrag) AS durchschnittsbetrag
FROM Kunden k
JOIN Bestellungen b ON k.kunde_id = b.kunde_id
WHERE k.stadt = 'Berlin'
GROUP BY k.name;
```

### Aufgabe 2: Produkt- und Lagerdatenbank

**Beschreibung:** Gegeben sind zwei Tabellen: `Produkte` und `Lager`.

- Tabelle `Produkte`: 
  - `produkt_id` (Primary Key)
  - `name`
  - `preis`

- Tabelle `Lager`: 
  - `lager_id` (Primary Key)
  - `produkt_id` (Foreign Key)
  - `menge`

**Aufgabe:** Schreibe ein SQL-Statement, das den Preis des teuersten Produkts im Lager aktualisiert und um 10% erhöht.

#### **Musterlösung:**
```sql
UPDATE Produkte
SET preis = preis * 1.10
WHERE produkt_id = (
    SELECT produkt_id
    FROM Produkte
    WHERE preis = (
        SELECT MAX(preis) FROM Produkte p JOIN Lager l ON p.produkt_id = l.produkt_id
    )
);
```

### Aufgabe 3: Mitarbeiter- und Abteilungsdatenbank

**Beschreibung:** Gegeben sind zwei Tabellen: `Mitarbeiter` und `Abteilungen`.

- Tabelle Mitarbeiter:
  - mitarbeiter_id (Primary Key)
  - name
  - abteilung_id (Foreign Key)
  
- Tabelle Abteilungen:
   - abteilung_id (Primary Key)
   - bezeichnung

**Aufgabe:** Schreibe eine Abfrage, die alle Mitarbeiter löscht, die in der Abteilung "Vertrieb" arbeiten.

#### **Musterlösung:**
```sql
DELETE FROM Mitarbeiter WHERE abteilung_id IN (
    SELECT abteilung_id FROM Abteilungen WHERE bezeichnung = 'Vertrieb'
);
```

### Aufgabe 4: Studentendatenbank

**Beschreibung:** Gegeben sind zwei Tabellen: Studenten und Noten.

- Tabelle Studenten:
   - student_id (Primary Key)
   - name

- Tabelle Noten:
   - note_id (Primary Key)
   - student_id (Foreign Key)
   - fach
   - note

**Aufgabe:** Schreibe eine SQL-Abfrage, die für jeden Studenten den Namen sowie die niedrigste Note in "Mathematik" ausgibt.

#### **Musterlösung:**
```sql
SELECT s.name, MIN(n.note) AS niedrigste_note_in_mathematik
FROM Studenten s 
JOIN Noten n ON s.student_id = n.student_id 
WHERE n.fach = 'Mathematik'
GROUP BY s.name;
```

Diese Aufgaben decken verschiedene Aspekte des Arbeitens mit relationalen Datenbanken mithilfe von SQL ab. Sie fördern das Verständnis von JOINs, Aggregatfunktionen sowie DML-Anweisungen wie UPDATE und DELETE.