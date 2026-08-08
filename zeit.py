def erzeuge_zeitachse():
    """
    Erzeugt 96 Zeitpunkte
    im Abstand von 15 Minuten.
    """

    zeiten = []

    for stunde in range(24):

        for minute in [0, 15, 30, 45]:

            zeiten.append(f"{stunde:02d}:{minute:02d}")

    return zeiten