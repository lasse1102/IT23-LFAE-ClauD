# Tic Tac Toe Spiel in Python
# Einfaches textbasiertes Spiel für Bildungszwecke

# Funktion zum Anzeigen des Spielbretts
def zeige_brett(brett):
    """
    Zeigt das aktuelle Spielbrett in der Konsole an
    brett: 2D-Array mit dem aktuellen Spielzustand
    """
    print("\n   0   1   2")  # Spalten-Nummern
    for i in range(3):
        print(f"{i}  {brett[i][0]} | {brett[i][1]} | {brett[i][2]}")
        if i < 2:  # Trennlinie zwischen den Zeilen (außer nach der letzten)
            print("  -----------")
    print()

# Funktion zum Überprüfen, ob ein Spieler gewonnen hat
def pruefe_gewinner(brett):
    """
    Überprüft alle möglichen Gewinnkombinationen
    Rückgabe: 'X' oder 'O' wenn jemand gewonnen hat, sonst None
    """
    # Überprüfe Zeilen
    for zeile in brett:
        if zeile[0] == zeile[1] == zeile[2] and zeile[0] != ' ':
            return zeile[0]
    
    # Überprüfe Spalten
    for spalte in range(3):
        if brett[0][spalte] == brett[1][spalte] == brett[2][spalte] and brett[0][spalte] != ' ':
            return brett[0][spalte]
    
    # Überprüfe Diagonalen
    # Hauptdiagonale (oben links nach unten rechts)
    if brett[0][0] == brett[1][1] == brett[2][2] and brett[0][0] != ' ':
        return brett[0][0]
    
    # Nebendiagonale (oben rechts nach unten links)
    if brett[0][2] == brett[1][1] == brett[2][0] and brett[0][2] != ' ':
        return brett[0][2]
    
    return None  # Kein Gewinner gefunden

# Funktion zum Überprüfen, ob das Brett voll ist (Unentschieden)
def ist_brett_voll(brett):
    """
    Überprüft, ob alle Felder belegt sind
    Rückgabe: True wenn voll, False wenn noch Plätze frei sind
    """
    for zeile in brett:
        for feld in zeile:
            if feld == ' ':
                return False
    return True

# Funktion für einen Spielzug
def mache_zug(brett, zeile, spalte, spieler):
    """
    Führt einen Spielzug aus, wenn das Feld frei ist
    Rückgabe: True wenn Zug erfolgreich, False wenn Feld bereits belegt
    """
    if brett[zeile][spalte] == ' ':
        brett[zeile][spalte] = spieler
        return True
    else:
        return False

# Hauptspiel-Funktion
def spiele_tic_tac_toe():
    """
    Hauptfunktion des Spiels - steuert den gesamten Spielablauf
    """
    # Initialisiere das Spielbrett als 3x3 Array mit Leerzeichen
    brett = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Aktueller Spieler (beginnt mit X)
    aktueller_spieler = 'X'
    
    print("=== TIC TAC TOE ===")
    print("Spieler X beginnt!")
    print("Gib die Koordinaten als 'Zeile Spalte' ein (0-2)")
    
    # Hauptspielschleife
    while True:
        # Zeige das aktuelle Brett
        zeige_brett(brett)
        
        # Frage nach dem nächsten Zug
        print(f"Spieler {aktueller_spieler} ist dran!")
        
        try:
            # Eingabe vom Spieler lesen
            eingabe = input("Gib Zeile und Spalte ein (z.B. '1 2'): ").split()
            
            # Überprüfe, ob genau zwei Zahlen eingegeben wurden
            if len(eingabe) != 2:
                print("Bitte gib genau zwei Zahlen ein!")
                continue
            
            zeile = int(eingabe[0])
            spalte = int(eingabe[1])
            
            # Überprüfe, ob die Koordinaten gültig sind (0-2)
            if zeile < 0 or zeile > 2 or spalte < 0 or spalte > 2:
                print("Koordinaten müssen zwischen 0 und 2 liegen!")
                continue
            
            # Versuche den Zug zu machen
            if mache_zug(brett, zeile, spalte, aktueller_spieler):
                # Überprüfe, ob jemand gewonnen hat
                gewinner = pruefe_gewinner(brett)
                if gewinner:
                    zeige_brett(brett)
                    print(f"🎉 Spieler {gewinner} hat gewonnen! 🎉")
                    break
                
                # Überprüfe auf Unentschieden
                if ist_brett_voll(brett):
                    zeige_brett(brett)
                    print("⚖️ Unentschieden! Das Brett ist voll.")
                    break
                
                # Wechsle zum anderen Spieler
                aktueller_spieler = 'O' if aktueller_spieler == 'X' else 'X'
            else:
                print("Dieses Feld ist bereits belegt! Wähle ein anderes.")
        
        except ValueError:
            print("Bitte gib nur Zahlen ein!")
        except KeyboardInterrupt:
            print("\nSpiel beendet.")
            break

# Hauptprogramm - wird nur ausgeführt, wenn die Datei direkt gestartet wird
if __name__ == "__main__":
    spiele_tic_tac_toe()
