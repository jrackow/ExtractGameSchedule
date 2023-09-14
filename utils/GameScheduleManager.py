import time

from selenium.webdriver.common.by import By
from utils.IcsManager import IcsManager
from selenium import webdriver


class Gameday:
    date = ""
    time = ""
    gameString = ""
    address = ""


class GameScheduleManager():

    def getGamedays(url, team, path):
        driver = webdriver.Chrome()
        GameScheduleManager.getCurrentGamedaySite(driver, url)
        driver.execute_script("document.getElementById('cmpbox').remove();")
        driver.execute_script("document.getElementById('cmpbox2').remove();")

        scheduleTable = driver.find_element(By.TAG_NAME, "table")
        scheduleItems = scheduleTable.find_elements(By.TAG_NAME, "tbody")

        gameList = []
        for scheduleItem in scheduleItems:
            rows = scheduleItem.find_elements(By.TAG_NAME, "td")
            gameday = Gameday()
            for row in rows:
                if "tw-spielplan-team" == row.get_attribute("class"):
                    teams = row.find_elements(By.TAG_NAME, "span")
                    homeTeam = teams[0].get_attribute("innerHTML")
                    awayTeam = teams[1].get_attribute("innerHTML")
                    if team in homeTeam or team in awayTeam:
                        gameday.gameString = homeTeam + " vs. " + awayTeam
                if "tw-spielplan-datum" == row.get_attribute("class"):
                    items = row.find_elements(By.TAG_NAME, "span")
                    for item in items:
                        if "hidden-xs ng-binding" in item.get_attribute("class"):
                            gameday.date = item.get_attribute("innerHTML").strip("&nbsp;&nbsp;&nbsp;")
                        if "tw-spielplan-uhrzeit" in item.get_attribute("class"):
                            gameday.time = item.get_attribute("innerHTML")
            if gameday.gameString:
                gameList.append(gameday)
        driver.quit()
        IcsManager.createIcsFile(gameList, team, path)

    def getCurrentGamedaySite(driver, url):
        driver.get(url)
        time.sleep(1)