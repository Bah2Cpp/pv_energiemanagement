def berechne_energiefluss(pv, lastprofil):
    """
    Berechnet den Energieüberschuss
    für alle 96 Messpunkte.
    """

    ueberschuss = []

    for pv_leistung, last in zip(pv, lastprofil):

        diff = pv_leistung - last

        ueberschuss.append(round(diff, 1))

    return ueberschuss