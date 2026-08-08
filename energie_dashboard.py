import matplotlib.pyplot as plt


def zeichne_energie_dashboard(
        zeiten,
        pv,
        lastprofil,
        netzbezug,
        einspeisung
):
    """
    Zeigt die wichtigsten Energieflüsse
    des PV-Energiemanagementsystems.
    """

    plt.figure(figsize=(14, 7))

    plt.plot(
        zeiten,
        pv,
        linewidth=2,
        label="PV-Leistung"
    )

    plt.plot(
        zeiten,
        lastprofil,
        linewidth=2,
        label="Hausverbrauch"
    )

    plt.plot(
        zeiten,
        netzbezug,
        linewidth=2,
        label="Netzbezug"
    )

    plt.plot(
        zeiten,
        einspeisung,
        linewidth=2,
        label="Netzeinspeisung"
    )

    plt.title("Energiemanagement – Energieflüsse")

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