def berechne_netz(ueberschuss, ladeverlauf):
    """
    Berechnet Netzbezug und Netzeinspeisung.

    Positiver Überschuss:
        Überschüssige PV-Leistung wird zuerst
        von der Batterie aufgenommen.
        Ist die Batterie voll, wird der Rest eingespeist.

    Negativer Überschuss:
        Die Batterie deckt zuerst das Defizit.
        Ist die Batterie leer, wird der Rest aus
        dem öffentlichen Netz bezogen.
    """

    KAPAZITAET = 10.0
    START_SOC = 5.0

    netzbezug = []
    einspeisung = []

    vorheriger_soc = START_SOC

    for diff, aktueller_soc in zip(ueberschuss, ladeverlauf):

        # Änderung des Batterieladezustands
        soc_aenderung = aktueller_soc - vorheriger_soc

        # ------------------------------------------------
        # PV-Überschuss
        # ------------------------------------------------

        if diff > 0:

            # Energie, die tatsächlich in die Batterie
            # aufgenommen wurde
            batterie_energie = max(soc_aenderung, 0)

            batterie_leistung = batterie_energie * 1000 / 0.25

            rest = diff - batterie_leistung

            if rest > 0:
                einspeisung.append(round(rest, 1))
            else:
                einspeisung.append(0)

            netzbezug.append(0)

        # ------------------------------------------------
        # PV-Defizit
        # ------------------------------------------------

        elif diff < 0:

            # Energie, die die Batterie abgegeben hat
            batterie_energie = min(soc_aenderung, 0)

            batterie_leistung = abs(
                batterie_energie * 1000 / 0.25
            )

            defizit = abs(diff)

            rest = defizit - batterie_leistung

            if rest > 0:
                netzbezug.append(round(rest, 1))
            else:
                netzbezug.append(0)

            einspeisung.append(0)

        # ------------------------------------------------
        # PV = Verbrauch
        # ------------------------------------------------

        else:

            netzbezug.append(0)
            einspeisung.append(0)

        vorheriger_soc = aktueller_soc

    return netzbezug, einspeisung