def simuliere_batterie(ueberschuss):
    """
    Simuliert einen Batteriespeicher.

    Kapazität:
        10 kWh

    Start:
        5 kWh
    """

    KAPAZITAET = 10.0      # kWh
    SOC = 5.0              # Startfüllstand

    ladezustand = []

    for diff in ueberschuss:

        # Leistung (W) -> Energie (kWh) für 15 Minuten
        energie = diff * 0.25 / 1000

        SOC += energie

        if SOC > KAPAZITAET:
            SOC = KAPAZITAET

        if SOC < 0:
            SOC = 0

        ladezustand.append(round(SOC, 2))

    return ladezustand