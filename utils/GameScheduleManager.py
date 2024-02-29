import json

from utils.IcsManager import IcsManager
from utils.functions.GetSpieldata import getSpieldata
from utils.functions.GetSpielorte import getSpielort


class Gameday:
    date = ""
    time = ""
    gameString = ""
    address = ""


class GameScheduleManager():
    def generate_ICS_File(url, team, path):
        spielData = GameScheduleManager.generateJsonData(url, team)
        IcsManager.createIcsFile(spielData, team, path)

    def generateJsonData(url, team):
        spielData = json.loads(getSpieldata(url=url, team=team))
        for data in spielData:
            # Spielorte hinzufügen
            spielort = getSpielort(url, data["Spiel-Nr."])
            data["Spielort"] = spielort
        return spielData


