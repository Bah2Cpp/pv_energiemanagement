import os
from datetime import datetime


def erstelle_bericht(auswertung):
    """
    Erstellt automatisch einen Projektbericht
    auf Basis der Simulationsergebnisse.
    """

    os.makedirs("berichte", exist_ok=True)

    datei = os.path.join(
        "berichte",
        "simulationsbericht.md"
    )

    with open(datei, "w", encoding="utf-8") as f:

        f.write("# PV-Energiemanagementsystem\n\n")

        f.write(
            "## Automatischer Simulationsbericht\n\n"
        )

        f.write(
            f"Erstellt am: {datetime.now():%d.%m.%Y %H:%M}\n\n"
        )

        f.write("---\n\n")

        f.write("## 1. Projektbeschreibung\n\n")

        f.write(
            "Dieser Bericht dokumentiert die Ergebnisse "
            "der Simulation eines PV-Energiemanagementsystems "
            "mit Batteriespeicher, Hausverbrauch und Netzanschluss.\n\n"
        )

        f.write("## 2. Simulationsergebnisse\n\n")

        f.write("| Kennzahl | Wert | Einheit |\n")
        f.write("|---|---:|---|\n")

        for name, wert in auswertung.items():

            if (
                "anteil" in name.lower()
                or "autarkie" in name.lower()
            ):
                einheit = "%"
            else:
                einheit = "kWh"

            f.write(
                f"| {name} | {wert:.2f} | {einheit} |\n"
            )

        f.write("\n")

        f.write("## 3. Bewertung\n\n")

        f.write(
            f"Die simulierte PV-Anlage erzeugte "
            f"{auswertung['PV-Erzeugung']:.2f} kWh Energie. "
        )

        f.write(
            f"Der Hausverbrauch betrug "
            f"{auswertung['Hausverbrauch']:.2f} kWh.\n\n"
        )

        f.write(
            f"Der Eigenverbrauchsanteil beträgt "
            f"{auswertung['Eigenverbrauchsanteil']:.2f} %. "
        )

        f.write(
            f"Der erreichte Autarkiegrad beträgt "
            f"{auswertung['Autarkiegrad']:.2f} %.\n\n"
        )

        f.write("## 4. Netz und Batterie\n\n")

        f.write(
            f"Aus dem öffentlichen Netz wurden "
            f"{auswertung['Netzbezug']:.2f} kWh bezogen. "
        )

        f.write(
            f"Ins Netz wurden "
            f"{auswertung['Netzeinspeisung']:.2f} kWh eingespeist.\n\n"
        )

        f.write(
            f"Die Batterie wurde mit "
            f"{auswertung['Batterie geladen']:.2f} kWh geladen "
            f"und mit "
            f"{auswertung['Batterie entladen']:.2f} kWh entladen.\n\n"
        )

        f.write("## 5. Fazit\n\n")

        f.write("## 5. Energiebilanz\n\n")

        f.write(
            "Die folgende Abbildung zeigt die Energiebilanz "
            "des simulierten PV-Energiemanagementsystems.\n\n"
        )

        f.write(
            "![Energiebilanz](../bilder/energiebilanz.png)\n\n"
        )

        f.write("## 6. Fazit\n\n")

        f.write(
            "Die Simulation zeigt die Energieflüsse zwischen "
            "PV-Anlage, Hausverbrauch, Batteriespeicher und "
            "öffentlichem Stromnetz. "
            "Die berechneten Kennzahlen ermöglichen eine "
            "Bewertung des Eigenverbrauchs und der energetischen "
            "Autarkie des Systems.\n"
        )
    print()
    print("=" * 50)
    print("BERICHT")
    print("=" * 50)
    print(f"Bericht gespeichert in: {datei}")