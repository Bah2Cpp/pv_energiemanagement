def berechne_energie(leistung):
    """
    Berechnet die Energie aus einer
    15-Minuten-Leistungsreihe.

    Leistung: W
    Rückgabe: kWh
    """

    energie = 0

    for wert in leistung:
        energie += wert * 0.25 / 1000

    return round(energie, 2)


def berechne_kennzahlen(
        pv,
        lastprofil,
        netzbezug,
        einspeisung
):
    """
    Berechnet die wichtigsten Energiekennzahlen.
    """

    pv_energie = berechne_energie(pv)

    verbrauch = berechne_energie(lastprofil)

    bezug = berechne_energie(netzbezug)

    einspeisung_energie = berechne_energie(einspeisung)

    return {
        "pv_energie": pv_energie,
        "verbrauch": verbrauch,
        "netzbezug": bezug,
        "einspeisung": einspeisung_energie
    }