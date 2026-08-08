def berechne_energiebilanz(
        pv,
        lastprofil,
        ladeverlauf
):
    """
    Berechnet die Energiebilanz des PV-Systems.

    Die Messwerte liegen im Abstand von 15 Minuten vor.
    """

    PV_ENERGIE = 0
    DIREKTER_EIGENVERBRAUCH = 0
    BATTERIE_LADUNG = 0
    BATTERIE_ENTLADUNG = 0
    HAUSVERBRAUCH = 0

    vorheriger_soc = 5.0

    for pv_leistung, last, soc in zip(
        pv,
        lastprofil,
        ladeverlauf
    ):

        # Zeitintervall: 15 Minuten
        zeit = 0.25

        # PV-Energie
        pv_energie = pv_leistung * zeit / 1000
        PV_ENERGIE += pv_energie

        # Hausverbrauch
        verbrauch = last * zeit / 1000
        HAUSVERBRAUCH += verbrauch

        # Direkter PV-Eigenverbrauch
        direkt = min(pv_leistung, last)

        DIREKTER_EIGENVERBRAUCH += (
            direkt * zeit / 1000
        )

        # Änderung des Batterie-SOC
        soc_aenderung = soc - vorheriger_soc

        # Batterie wird geladen
        if soc_aenderung > 0:

            BATTERIE_LADUNG += soc_aenderung

        # Batterie wird entladen
        elif soc_aenderung < 0:

            BATTERIE_ENTLADUNG += abs(
                soc_aenderung
            )

        vorheriger_soc = soc

    # PV-Energie, die insgesamt selbst genutzt wurde
    eigenverbrauch = (
        DIREKTER_EIGENVERBRAUCH
        + BATTERIE_ENTLADUNG
    )

    # Eigenverbrauchsanteil
    if PV_ENERGIE > 0:
        eigenverbrauchsanteil = (
            eigenverbrauch / PV_ENERGIE
        ) * 100
    else:
        eigenverbrauchsanteil = 0

    # Autarkiegrad
    if HAUSVERBRAUCH > 0:
        autarkiegrad = (
            eigenverbrauch / HAUSVERBRAUCH
        ) * 100
    else:
        autarkiegrad = 0

    return {
        "pv_energie": round(PV_ENERGIE, 2),
        "hausverbrauch": round(HAUSVERBRAUCH, 2),
        "direkter_eigenverbrauch": round(
            DIREKTER_EIGENVERBRAUCH, 2
        ),
        "batterie_ladung": round(
            BATTERIE_LADUNG, 2
        ),
        "batterie_entladung": round(
            BATTERIE_ENTLADUNG, 2
        ),
        "eigenverbrauch": round(
            eigenverbrauch, 2
        ),
        "eigenverbrauchsanteil": round(
            eigenverbrauchsanteil, 2
        ),
        "autarkiegrad": round(
            autarkiegrad, 2
        )
    }