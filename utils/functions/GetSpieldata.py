import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
def getSpieldata(url, team):

    # WebDriver Service initialisieren
    service = Service(ChromeDriverManager().install())

    # Optionen für den WebDriver (optional)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Headless-Modus, falls keine GUI benötigt wird

    # WebDriver initialisieren
    driver = webdriver.Chrome(service=service, options=options)

    # URL öffnen
    driver.get(url)

    # Warten, um sicherzustellen, dass die Seite vollständig geladen wurde
    time.sleep(5)  # Pausieren für 5 Sekunden; Anpassung je nach Ladezeit der Seite

    # Den vollständig geladenen Seiteninhalt erhalten
    html_content = driver.page_source

    # BeautifulSoup Objekt initialisieren
    soup = BeautifulSoup(html_content, 'html.parser')

    # Versuchen, die Tabelle zu finden (Anpassung der Klassenbezeichnung erforderlich)
    table = soup.find('table', {'class': 'table tw-spielplan tw-no-stripes'})

    # Liste initialisieren, um die extrahierten Daten zu speichern
    data = []

    # Über jede Zeile der Tabelle iterieren, außer der Kopfzeile
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            # Zuerst die Werte für Gast und Heim extrahieren und bereinigen
            gast = cols[4].text.strip() if len(cols) > 4 else ''
            heim_raw = cols[2].text.strip() if len(cols) > 2 else ''

            # Den Gast-String vom Heim-String entfernen, falls vorhanden
            if gast and heim_raw.endswith(gast):
                heim = heim_raw.rsplit(gast, 1)[0].strip()
            else:
                heim = heim_raw  # Falls Gast nicht am Ende von Heim steht, bleibt Heim unverändert

            # Extrahieren des Datums und der Uhrzeit
            datum_zeit_string = cols[0].text.strip()
            datum_zeit_teile = datum_zeit_string.split(' ', 2)  # Maximal 2 Teile erwarten: Datum und Uhrzeit
            if len(datum_zeit_teile) >= 2:
                datum, uhrzeit = datum_zeit_teile[0], datum_zeit_teile[1]
            else:
                datum, uhrzeit = datum_zeit_teile[0], ""

            if heim == team or gast == team:
                # Erstellen eines temporären Dictionaries für die aktuelle Zeile
                row_data = {
                    'Datum': datum.strip(),
                    'Uhrzeit': uhrzeit.strip(),
                    'Spiel-Nr.': cols[1].text.strip() if len(cols) > 1 else '',
                    'Heim': heim,
                    'Ergebnis': cols[3].text.strip() if len(cols) > 3 else '',
                    'Gast': gast,
                }

                # Überprüfen, ob alle Werte im row_data gefüllt sind
                if all(value for value in row_data.values()):
                    data.append(row_data)

    # Die Daten in JSON umwandeln
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    # Den WebDriver schließen
    driver.quit()

    return json_data