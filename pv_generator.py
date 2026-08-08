import math


def erzeuge_pv_profil():

    """
    Erzeugt ein einfaches PV-Profil
    mit 96 Messpunkten.
    """

    pv = []

    MAX_LEISTUNG = 4500

    for i in range(96):

        stunde = i / 4

        if 6 <= stunde <= 18:

            winkel = math.pi * (stunde - 6) / 12

            leistung = MAX_LEISTUNG * math.sin(winkel)

            leistung = max(0, leistung)

        else:

            leistung = 0

        pv.append(round(leistung, 1))

    return pv