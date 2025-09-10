# Test-Version des Tic Tac Toe Spiels
# Um Eingabe-Probleme zu identifizieren

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

# Test der Grundfunktionen
def test_spiel():
    """
    Testet die Grundfunktionen ohne interaktive Eingabe
    """
    print("=== TIC TAC TOE TEST ===")
    
    # Initialisiere das Spielbrett
    brett = [[' ' for _ in range(3)] for _ in range(3)]
    print("Leeres Brett erstellt:")
    zeige_brett(brett)
    
    # Teste einige Züge
    brett[0][0] = 'X'
    brett[1][1] = 'O'
    brett[0][1] = 'X'
    brett[2][0] = 'O'
    brett[0][2] = 'X'
    
    print("Nach einigen Test-Zügen:")
    zeige_brett(brett)
    
    print("Test erfolgreich abgeschlossen!")
    
    # Teste input() Funktion
    print("\nTeste input() Funktion...")
    try:
        test_eingabe = input("Bitte gib etwas ein (Test): ")
        print(f"Eingabe erhalten: '{test_eingabe}'")
    except Exception as e:
        print(f"Fehler bei input(): {e}")

if __name__ == "__main__":
    test_spiel()
