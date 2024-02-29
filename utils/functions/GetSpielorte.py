from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
def getSpielort(url, spielNr):
    # WebDriver Service initialisieren
    service = Service(ChromeDriverManager().install())

    # Optionen für den WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Headless-Modus

    # WebDriver initialisieren
    driver = webdriver.Chrome(service=service, options=options)

    # URL der Spieleliste öffnen
    driver.get(url)

    time.sleep(2)
    popup = driver.find_element(By.CLASS_NAME, "cmptxt_btn_yes")
    popup.click()

    xpath_expression = "//td[contains(@class, 'tw-spielplan-spielnr') and contains(text(), '"+spielNr+"')]"

    # Warten auf das Element und es dann suchen
    spiel_nr_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath_expression))
    )
    spiel_nr_element.click()

    # Kurze Pause, um das Laden der Detailansicht abzuwarten
    time.sleep(2)  # Pausieren für 2 Sekunden; Anpassung je nach Ladezeit

    # Informationen aus der Detailansicht extrahieren
    ort = driver.find_element(By.CSS_SELECTOR, "span.tw-block[ng-bind='sportstaette.bezeichnung']").text
    strasse = driver.find_element(By.CSS_SELECTOR, "span.tw-block[ng-bind='sportstaette.strasse']").text
    plz_stadt = driver.find_elements(By.CSS_SELECTOR, "span.tw-block")[2].text

    # Browser schließen
    driver.quit()
    # Ort, Straße und PLZ/Stadt zurückgeben
    return {
        'Ort': ort,
        'Straße': strasse,
        'PLZ und Stadt': plz_stadt
    }