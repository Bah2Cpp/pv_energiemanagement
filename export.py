import csv
import os


def exportiere_ergebnisse(auswertung):
    """
    Speichert die Auswertung des PV-Energiemanagementsystems
    als CSV-Datei.
    """

    os.makedirs("export", exist_ok=True)

    datei = os.path.join("export", "energiebilanz.csv")

    with open(datei, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["Kennzahl", "Wert", "Einheit"])

        for name, wert in auswertung.items():

            if "anteil" in name.lower() or "autarkie" in name.lower():
                einheit = "%"
            else:
                einheit = "kWh"

            writer.writerow([
                name,
                round(wert, 2),
                einheit
            ])

    print()
    print("=" * 50)
    print("EXPORT")
    print("=" * 50)
    print(f"Ergebnisse gespeichert in: {datei}")