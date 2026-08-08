import matplotlib.pyplot as plt


def zeichne_pv(zeiten, pv):

    plt.figure(figsize=(14,6))

    plt.plot(
        zeiten,
        pv,
        color="orange",
        linewidth=2,
        label="PV-Leistung"
    )

    plt.title("PV-Leistungsprofil")

    plt.xlabel("Zeit")

    plt.ylabel("Leistung [W]")

    plt.grid(True)

    plt.xticks(
        range(0,96,4),
        zeiten[::4],
        rotation=45
    )

    plt.legend()

    plt.tight_layout()

    plt.show()