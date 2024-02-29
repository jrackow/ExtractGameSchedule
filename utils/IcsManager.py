from datetime import datetime, timedelta

from icalendar import Calendar, Event
class IcsManager:

    def createIcsFile(spielData, team, path):
        spielCalendar = Calendar()

        for spiel in spielData:

            # Daten vorbereiten
            date_time_string = spiel["Datum"] + " " + spiel["Uhrzeit"]
            date_time = datetime.strptime(date_time_string, "%d.%m.%Y %H:%M")
            start = date_time
            end = date_time + timedelta(hours=2)

            # Erstellen des Kalendar Events
            e = Event()
            e.add("summary", spiel["Heim"]+ " vs. " + spiel["Gast"])
            e.add("dtstart", start)
            e.add("dtend", end)
            e.add("location", spiel["Spielort"]["Straße"] + ", " + spiel["Spielort"]["PLZ und Stadt"])
            spielCalendar.add_component(e)
        # Schreiben der ICS Datei für den Heimkalendar
        f = open(path + '/' + team + '.ics', 'wb')
        f.write(spielCalendar.to_ical())
        f.close()
