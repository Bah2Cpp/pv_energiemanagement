from zeit import erzeuge_zeitachse

from pv_generator import erzeuge_pv_profil

from pv_diagramm import zeichne_pv

from lastprofil_generator import erzeuge_lastprofil

from energiefluss import zeichne_energiefluss

from energie_berechnung import berechne_energiefluss
from batterie import simuliere_batterie

from energie_berechnung import berechne_energiefluss
from batterie import simuliere_batterie
from netz import berechne_netz
from energie_dashboard import zeichne_energie_dashboard
from batterie_diagramm import zeichne_batterie_soc

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

    zeichne_batterie_soc(
        zeiten,
        ladeverlauf
    )

    netzbezug, einspeisung = berechne_netz(
        ueberschuss,
        ladeverlauf
    )

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