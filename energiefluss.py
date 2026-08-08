import matplotlib.pyplot as plt


def zeichne_energiefluss(zeiten, pv, lastprofil):
    """
    Zeichnet PV-Leistung und Hausverbrauch
    in einem gemeinsamen Diagramm.
    """

    plt.figure(figsize=(14, 6))

    plt.plot(
        zeiten,
        pv,
        color="orange",
        linewidth=2,
        label="PV-Leistung"
    )

    plt.plot(
        zeiten,
        lastprofil,
        color="blue",
        linewidth=2,
        label="Hausverbrauch"
    )

    plt.title("PV-Leistung und Hausverbrauch")

    plt.xlabel("Zeit")

    plt.ylabel("Leistung [W]")

    plt.xticks(
        range(0, 96, 4),
        zeiten[::4],
        rotation=45
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()