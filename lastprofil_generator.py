import random


def erzeuge_lastprofil():
    """
    Erzeugt ein realistisches Lastprofil
    eines Einfamilienhauses.

    96 Messpunkte (15 Minuten)
    """

    lastprofil = []

    for i in range(96):

        stunde = i / 4

        # Nacht
        if stunde < 6:
            leistung = random.randint(150, 300)

        # Morgen
        elif stunde < 8:
            leistung = random.randint(1800, 2800)

        # Vormittag
        elif stunde < 12:
            leistung = random.randint(300, 700)

        # Mittag
        elif stunde < 14:
            leistung = random.randint(700, 1800)

        # Nachmittag
        elif stunde < 17:
            leistung = random.randint(300, 700)

        # Abend
        elif stunde < 21:
            leistung = random.randint(2200, 3500)

        # Nacht
        else:
            leistung = random.randint(200, 400)

        lastprofil.append(leistung)

    return lastprofil