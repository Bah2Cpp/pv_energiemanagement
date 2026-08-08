from zeit import erzeuge_zeitachse

from pv_generator import erzeuge_pv_profil

from pv_diagramm import zeichne_pv

from lastprofil_generator import erzeuge_lastprofil

from energiefluss import zeichne_energiefluss

from energie_berechnung import berechne_energiefluss
from batterie import simuliere_batterie
from netz import berechne_netz
from energie_dashboard import zeichne_energie_dashboard
from batterie_diagramm import zeichne_batterie_soc
from energie_kennzahlen import berechne_kennzahlen
from energiebilanz import berechne_energiebilanz
from energiebilanz_diagramm import zeichne_energiebilanz
from auswertung import erstelle_auswertung
from export import exportiere_ergebnisse
from bericht import erstelle_bericht
from pdf_bericht import erstelle_pdf_bericht




def main():

    # ---------------------------------------------------
    # 1. Zeitachse erzeugen
    # ---------------------------------------------------

    zeiten = erzeuge_zeitachse()

    # ---------------------------------------------------
    # 2. PV-Leistungsprofil erzeugen
    # ---------------------------------------------------

    pv = erzeuge_pv_profil()

    # ---------------------------------------------------
    # 3. Hausverbrauch erzeugen
    # ---------------------------------------------------

    lastprofil = erzeuge_lastprofil()

    ueberschuss = berechne_energiefluss(
        pv,
        lastprofil
    )

    ladeverlauf = simuliere_batterie(
        ueberschuss
    )

    ueberschuss = berechne_energiefluss(
        pv,
        lastprofil
    )

    ladeverlauf = simuliere_batterie(
        ueberschuss
    )

    energiebilanz = berechne_energiebilanz(
        pv,
        lastprofil,
        ladeverlauf
    )

    netzbezug, einspeisung = berechne_netz(
        ueberschuss,
        ladeverlauf
    )

    kennzahlen = berechne_kennzahlen(
        pv,
        lastprofil,
        netzbezug,
        einspeisung
    )
    print()
    print("DEBUG ENERGIEBILANZ:")
    print("SCHLÜSSEL DER ENERGIEBILANZ:")
    print(energiebilanz.keys())

    print()
    print("DEBUG KENNZAHLEN:")
    print(kennzahlen.keys())

    auswertung = erstelle_auswertung(
        energiebilanz,
        kennzahlen
    )

    exportiere_ergebnisse(auswertung)

    erstelle_bericht(auswertung)

    erstelle_pdf_bericht(auswertung)

    print()
    print("=" * 50)
    print("GESAMTAUSWERTUNG")
    print("=" * 50)

    for name, wert in auswertung.items():

        if "anteil" in name.lower() or "autarkie" in name.lower():
            print(f"{name:<25}: {wert:.2f} %")
        else:
            print(f"{name:<25}: {wert:.2f} kWh")

    zeichne_energiebilanz(
        energiebilanz["pv_energie"],
        energiebilanz["hausverbrauch"],
        energiebilanz["eigenverbrauch"],
        kennzahlen["netzbezug"],
        kennzahlen["einspeisung"]
    )

    print()
    print("=" * 50)
    print("ENERGIEBILANZ")
    print("=" * 50)

    print(
        f"PV-Energie              : "
        f"{energiebilanz['pv_energie']:.2f} kWh"
    )

    print(
        f"Hausverbrauch           : "
        f"{energiebilanz['hausverbrauch']:.2f} kWh"
    )

    print(
        f"Direkter Eigenverbrauch : "
        f"{energiebilanz['direkter_eigenverbrauch']:.2f} kWh"
    )

    print(
        f"Batterie geladen        : "
        f"{energiebilanz['batterie_ladung']:.2f} kWh"
    )

    print(
        f"Batterie entladen       : "
        f"{energiebilanz['batterie_entladung']:.2f} kWh"
    )

    print(
        f"Eigenverbrauch          : "
        f"{energiebilanz['eigenverbrauch']:.2f} kWh"
    )

    print(
        f"Eigenverbrauchsanteil   : "
        f"{energiebilanz['eigenverbrauchsanteil']:.2f} %"
    )

    print(
        f"Autarkiegrad            : "
        f"{energiebilanz['autarkiegrad']:.2f} %"
    )

    zeichne_batterie_soc(
        zeiten,
        ladeverlauf
    )

    netzbezug, einspeisung = berechne_netz(
        ueberschuss,
        ladeverlauf
    )

    kennzahlen = berechne_kennzahlen(
        pv,
        lastprofil,
        netzbezug,
        einspeisung
    )

    print()
    print("=" * 50)
    print("ENERGIEKENNZAHLEN")
    print("=" * 50)

    print(f"PV-Energie        : {kennzahlen['pv_energie']:.2f} kWh")
    print(f"Hausverbrauch     : {kennzahlen['verbrauch']:.2f} kWh")
    print(f"Netzbezug         : {kennzahlen['netzbezug']:.2f} kWh")
    print(f"Netzeinspeisung   : {kennzahlen['einspeisung']:.2f} kWh")

    zeichne_energie_dashboard(
        zeiten,
        pv,
        lastprofil,
        netzbezug,
        einspeisung
    )

    print()
    print("=" * 50)
    print("NETZBEZUG UND NETZEINSPEISUNG")
    print("=" * 50)

    for i in range(96):
        print(
            f"{zeiten[i]} | "
            f"Netzbezug: {netzbezug[i]:7.1f} W | "
            f"Einspeisung: {einspeisung[i]:7.1f} W"
        )
    # ---------------------------------------------------
    # 4. PV-Diagramm anzeigen
    # ---------------------------------------------------

    zeichne_pv(
        zeiten,
        pv
    )

    # ---------------------------------------------------
    # 5. PV und Hausverbrauch vergleichen
    # ---------------------------------------------------

    zeichne_energiefluss(
        zeiten,
        pv,
        lastprofil
    )

    print()
    print("=" * 50)
    print("BATTERIE")
    print("=" * 50)

    for i in range(10):
        print(
            f"{zeiten[i]} | "
            f"Überschuss: {ueberschuss[i]:7.1f} W | "
            f"Batterie: {ladeverlauf[i]:5.2f} kWh"
        )

# -------------------------------------------------------
# Programmstart
# -------------------------------------------------------

if __name__ == "__main__":
    main()