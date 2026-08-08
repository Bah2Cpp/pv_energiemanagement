import matplotlib.pyplot as plt
import os

def zeichne_energiebilanz(
        pv_energie,
        hausverbrauch,
        eigenverbrauch,
        netzbezug,
        einspeisung
):
    """
    Erstellt ein Balkendiagramm der wichtigsten
    Energiegrößen des Systems.
    """

    namen = [
        "PV-Erzeugung",
        "Hausverbrauch",
        "Eigenverbrauch",
        "Netzbezug",
        "Netzeinspeisung"
    ]

    werte = [
        pv_energie,
        hausverbrauch,
        eigenverbrauch,
        netzbezug,
        einspeisung
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(namen, werte)

    plt.title("Energiebilanz des PV-Energiemanagementsystems")

    plt.ylabel("Energie [kWh]")

    plt.xlabel("Energiegröße")

    plt.grid(
        axis="y",
        alpha=0.3
    )

    plt.xticks(rotation=20)

    plt.tight_layout()

    os.makedirs("bilder", exist_ok=True)

    plt.savefig(
        "bilder/energiebilanz.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()