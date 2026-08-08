def erstelle_auswertung(energiebilanz, kennzahlen):
    """
    Erstellt eine übersichtliche Gesamtauswertung
    des PV-Energiemanagementsystems.
    """

    auswertung = {
        "PV-Erzeugung": energiebilanz["pv_energie"],
        "Hausverbrauch": energiebilanz["hausverbrauch"],
        "Direkter Eigenverbrauch": energiebilanz["direkter_eigenverbrauch"],
        "Batterie geladen": energiebilanz["batterie_ladung"],
        "Batterie entladen": energiebilanz["batterie_entladung"],
        "Netzbezug": kennzahlen["netzbezug"],
        "Netzeinspeisung": kennzahlen["einspeisung"],
        "Eigenverbrauchsanteil": energiebilanz["eigenverbrauchsanteil"],
        "Autarkiegrad": energiebilanz["autarkiegrad"]
    }

    return auswertung