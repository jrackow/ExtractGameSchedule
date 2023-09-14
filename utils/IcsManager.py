from datetime import datetime, timedelta

from icalendar import Calendar, Event
class IcsManager:

    def createIcsFile(gameList, team, path):
        home = Calendar()
        away = Calendar()

        for game in gameList:
            # Daten vorbereiten
            date_time_string = game.date + " " + game.time
            date_time = datetime.strptime(date_time_string, "%d.%m.%Y %H:%M")
            start = date_time
            end = date_time + timedelta(hours=2)

            # Erstellen des Kalendar Events
            e = Event()
            e.add("summary", game.gameString)
            e.add("dtstart", start)
            e.add("dtend", end)

            # Schreiben in den Heim oder Auswärtskalendar
            teams = game.gameString.split("vs.")
            if team in teams[0]:
                home.add_component(e)
            elif team in teams[1]:
                away.add_component(e)
        print(path)
        # Schreiben der ICS Datei für den Heimkalendar
        f = open(path + '/' + team + ' Heim.ics', 'wb')
        f.write(home.to_ical())
        f.close()

        #Schreiben der ICS Datei für den Auswärtskalendar
        f = open(path + '/' + team + ' Auswärts.ics', 'wb')
        f.write(away.to_ical())
        f.close()