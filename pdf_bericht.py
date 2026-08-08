import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)



def erstelle_pdf_bericht(auswertung):

    os.makedirs("berichte", exist_ok=True)

    datei = os.path.join(
        "berichte",
        "simulationsbericht.pdf"
    )

    doc = SimpleDocTemplate(
        datei,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    styles = getSampleStyleSheet()

    titel = styles["Title"]
    ueberschrift = styles["Heading2"]
    text = styles["BodyText"]

    inhalt = []

    # Titel
    inhalt.append(
        Paragraph(
            "PV-Energiemanagementsystem",
            titel
        )
    )

    inhalt.append(Spacer(1, 0.5 * cm))

    inhalt.append(
        Paragraph(
            "Automatischer Simulationsbericht",
            ueberschrift
        )
    )

    inhalt.append(Spacer(1, 0.5 * cm))

    # Projektbeschreibung
    inhalt.append(
        Paragraph(
            "1. Projektbeschreibung",
            ueberschrift
        )
    )

    inhalt.append(
        Paragraph(
            "Dieser Bericht dokumentiert die Ergebnisse "
            "der Simulation eines PV-Energiemanagementsystems "
            "mit PV-Anlage, Hausverbrauch, Batteriespeicher "
            "und Netzanschluss.",
            text
        )
    )

    inhalt.append(Spacer(1, 0.5 * cm))

    # Ergebnisse
    inhalt.append(
        Paragraph(
            "2. Simulationsergebnisse",
            ueberschrift
        )
    )

    daten = [
        ["Kennzahl", "Wert", "Einheit"]
    ]

    for name, wert in auswertung.items():

        if (
            "anteil" in name.lower()
            or "autarkie" in name.lower()
        ):
            einheit = "%"
        else:
            einheit = "kWh"

        daten.append([
            name,
            f"{wert:.2f}",
            einheit
        ])

    tabelle = Table(
        daten,
        colWidths=[9 * cm, 4 * cm, 3 * cm]
    )

    tabelle.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("TOPPADDING", (0, 0), (-1, 0), 8),
        ])
    )

    inhalt.append(tabelle)

    inhalt.append(Spacer(1, 0.8 * cm))

    # Diagramm
    inhalt.append(
        Paragraph(
            "3. Energiebilanz",
            ueberschrift
        )
    )

    inhalt.append(
        Paragraph(
            "Die folgende Abbildung zeigt die Energiebilanz "
            "des simulierten Systems.",
            text
        )
    )

    inhalt.append(Spacer(1, 0.3 * cm))

    bilddatei = os.path.join(
        "bilder",
        "energiebilanz.png"
    )

    if os.path.exists(bilddatei):

        bild = Image(
            bilddatei,
            width=16 * cm,
            height=9 * cm
        )

        inhalt.append(bild)

    else:

        inhalt.append(
            Paragraph(
                "Das Energiebilanz-Diagramm wurde nicht gefunden.",
                text
            )
        )

    inhalt.append(Spacer(1, 0.8 * cm))

    # Bewertung
    inhalt.append(
        Paragraph(
            "4. Bewertung",
            ueberschrift
        )
    )

    inhalt.append(
        Paragraph(
            f"Die PV-Anlage erzeugte "
            f"{auswertung['PV-Erzeugung']:.2f} kWh. "
            f"Der Hausverbrauch betrug "
            f"{auswertung['Hausverbrauch']:.2f} kWh.",
            text
        )
    )

    inhalt.append(Spacer(1, 0.3 * cm))

    inhalt.append(
        Paragraph(
            f"Der Eigenverbrauchsanteil beträgt "
            f"{auswertung['Eigenverbrauchsanteil']:.2f} %. "
            f"Der Autarkiegrad beträgt "
            f"{auswertung['Autarkiegrad']:.2f} %.",
            text
        )
    )

    inhalt.append(Spacer(1, 0.5 * cm))

    # Fazit
    inhalt.append(
        Paragraph(
            "5. Fazit",
            ueberschrift
        )
    )

    inhalt.append(
        Paragraph(
            "Die Simulation ermöglicht die Untersuchung "
            "der Energieflüsse zwischen PV-Anlage, "
            "Hausverbrauch, Batteriespeicher und öffentlichem "
            "Stromnetz. Die berechneten Kennzahlen dienen "
            "zur Bewertung des Eigenverbrauchs und der "
            "energetischen Autarkie.",
            text
        )
    )

    doc.build(inhalt)

    print()
    print("=" * 50)
    print("PDF-BERICHT")
    print("=" * 50)
    print(f"PDF gespeichert in: {datei}")