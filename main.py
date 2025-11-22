# main.py
from db_utils import init_db, clear_locations, add_location, get_locations
from datetime import datetime

LOGFILE = "lokitiedosto.txt"

def append_log(line: str):
    ts = datetime.now().isoformat()
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{ts} — {line}\n")

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
        if not val:
            continue
        if val.upper() == "X":
            break
        add_location(val)
        print(f"Lisätty: {val}")
    print("Syöttö päättyi.")
    append_log("Paikkakunnat päivitetty")

def main():
    init_db()
    input_locations_loop()
    print(get_locations())
    # Далее: спросить про haun и т.д.

if __name__ == "__main__":
    main()