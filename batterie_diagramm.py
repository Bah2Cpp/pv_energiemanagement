import matplotlib.pyplot as plt


def zeichne_batterie_soc(zeiten, ladeverlauf):
    """
    Zeigt den Ladezustand der Batterie
    über den Tagesverlauf.

    ladeverlauf wird in kWh übergeben.
    """

    kapazitaet = 10.0

    soc = []

    for ladezustand in ladeverlauf:

        prozent = (ladezustand / kapazitaet) * 100

        soc.append(prozent)

    plt.figure(figsize=(14, 6))

    plt.plot(
        zeiten,
        soc,
        linewidth=2,
        label="Batterie-SOC"
    )

    plt.title("Batterie-Ladezustand")

    plt.xlabel("Zeit")

    plt.ylabel("SOC [%]")

    plt.xticks(
        range(0, 96, 4),
        zeiten[::4],
        rotation=45
    )

    plt.ylim(0, 100)

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()