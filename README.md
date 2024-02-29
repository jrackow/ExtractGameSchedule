# Extract Game Schedule

Eine Anwendung, mit der sich Spielpläne von der Website [www.basketball-bund.net](http://www.basketball-bund.net/) in ICS exportieren lassen.

## Anleitung
- Anwendung [herunterladen](https://github.com/jrackow/ExtractGameSchedule/releases/tag/basketball) und ausführen
- Team und Link eintragen
	- *Team muss dem genauen Namen auf der Website entsprechen*
	- *Url muss auf die Spielplan-Seite zeigen. Beispiel: https://www.basketball-bund.net/static/#/liga/NUMMER/spielplan*
- Auf Exportieren drücken und den Ordner für die ICS Dateien auswählen.
- Es werden eine ICS Datei mit den Spielen generiert. 

*Die Erstellung der ICS Datei, kann je nach Größe der Liga bis zu 5min in Anspruch nehmen*
## Windows EXE erstellen
`pyinstaller --noconsole --onefile main.py`
## Kontakt
Für Anregungen oder Fragen stehe ich unter: jolen@simplebug.de zur Verfügung.