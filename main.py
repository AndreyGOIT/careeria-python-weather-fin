# main.py
from db_utils import init_db, clear_locations, add_location, get_locations
from datetime import datetime
from weather_fetcher import hae_lampotila

LOGFILE = "lokitiedosto.txt"

# Append a line to the log file with a timestamp
def append_log(line: str):
    ts = datetime.now().isoformat()
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{ts} — {line}\n")

# Input loop to modify tracked locations
def input_locations_loop():
    print("Haluan muuttaa seurattavia paikkakuntia? (K = kyllä, muuta = ei)")
    answer = input().strip().upper()
    if answer != "K":
        print("Paikkakuntia ei muutettu.")
        return

    clear_locations()
    print("Anna paikkakuntien nimet, yksi per rivi. Lopeta kirjoittamalla 'X' ja paina Enter.")
    while True:
        val = input("Paikkakunta (tai X lopettaa): ").strip()
        if val.upper() == "X":
            break
        if val:
            add_location(val)
            print(f"Lisätty: {val}")
    append_log("Paikkakunnat päivitetty")
    print("Syöttö päättyi.")

# Main program logic
def main():
    init_db()
    input_locations_loop()

    paikat = get_locations()
    if not paikat:
        print("Ei seurattavia paikkakuntia. Lopetetaan.")
        return
    print(paikat)

    print("\nHaetaan lämpötilat...\n")

    onnistuneet = 0
    for paikka in paikat:
        lampotila = hae_lampotila(paikka)

        if lampotila is None:
            print(f"{paikka:<15} Hakuvirhe")
            append_log(f"{paikka} — Hakuvirhe")
        else:
            print(f"{paikka:<15} {lampotila:.1f} °C")
            onnistuneet += 1
            append_log(f"{paikka} — {lampotila:.1f} °C")
    
    print(f"\nLämpötilahaut suoritettu. Haettu onnistuneesti: {onnistuneet} paikkakuntaa.")
    append_log(f"Haettu onnistuneesti: {onnistuneet} paikkakuntaa.")

# Run the main function
if __name__ == "__main__":
    main()