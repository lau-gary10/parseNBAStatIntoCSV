'''
This file will convert listed data into a csv file.
Player Tracking:
    Speed and Distance
    Touch and Possession
    Passing
    Defensive Impact
    Rebounding Opportunities
    Drives
    Catch And Shoot
    Pull Up
    Shooting Efficiency
Total Statistics 2013-14
    Atlanta Hawks
    Boston Celtics
    Brooklyn Nets
    Charlotte Bobcats
    Chicago Bulls
    Cleveland Cavaliers
    Dallas Mavericks
    Denver Nuggets
    Detroit Pistons
    Golden State Warriors
    Houston Rockets
    Indiana Pacers
    Los Angeles Clippers
    Los Angeles Lakers
    Memphis Grizzlies
    Miami Heat
    Milwaukee Bucks
    Minnesota Timberwolves
    New Orleans Pelicans
    New York Knicks
    Oklahoma City Thunder
    Orlando Magic
    Philadelphia 76ers
    Phoenix Suns
    Portland Trail Blazers
    Sacramento Kings
    San Antonio Spurs
    Toronto Raptors
    Utah Jazz
    Washington Wizards

'''

import urllib.request
import os
import time

nbaFileDir = "C:/Users/glau/Downloads/nbaSpreadsheets/"
openFilename = "default"
saveFilename = "default"
urlAddr = "default"

seasonStr = "default"
teamID = "default"
urlAddrTotalStats = "default"
totalStatFilename = "NBA Total Statistics.csv"


# Open downloaded file
def openFile(filename):
    with open(filename) as myfile:
        data = myfile.read()
        myfile.close()
    return data

# Parse through downloaded Player Tracking file for csv conversion
def parseDataReadPlayerTracking(data):
# Cut out all the string prior to ' "headers" '
    startPos = data.find('"headers"')
    endPos = data.__len__()
    dataStr = data[startPos:endPos]
# Find and delete string ' "headers":[ '
    dataStr = dataStr.replace('"headers":[', '')
# Find and delete string ' "rowset":[ '
    dataStr = dataStr.replace('"rowSet":[', '')
# Cut out all the string after ' ]] '
    startPos = 0
    endPos = dataStr.find(']]')
    dataStr = dataStr[startPos:endPos]
# Replace ' ] ' with newline character
    dataStr = dataStr.replace("]", '\n')
# Delete ' ,[ '
    dataStr = dataStr.replace(",[", '')
    return dataStr

# Parse through downloaded Total Statistics file for csv conversion
def parseDataReadTotalStatistics(data):
# Cut out all the string prior to ' "PlayersSeasonTotals" '
    startPos = data.find('"PlayersSeasonTotals"')
    endPos = data.__len__()
    dataStr = data[startPos:endPos]
# Find and delete string ' "headers":[ '
    dataStr = dataStr.replace('"headers":[', '')
# Find and delete string ' "rowset":[ '
    dataStr = dataStr.replace('"rowSet":[', '')
# Cut out all the string after ' ]] '
    startPos = 0
    endPos = dataStr.find(']]')
    dataStr = dataStr[startPos:endPos]
# Replace ' ] ' with newline character
    dataStr = dataStr.replace("]", '\n')
# Delete ' ,[ '
    dataStr = dataStr.replace(",[", '')
    return dataStr

# Write parsed string into a new csv file
def writeFile(dataStr, filename, openModeArg):
    # Write dataStr to a new file
    target = open(nbaFileDir + filename, openModeArg)
    target.write(dataStr)
    target.close
    return

# Takes downloaded data and translate it into csv file
def parseNBADataIntoCSV(startFilename, endFilename, IDTypeNum):
    tmpData = openFile(nbaFileDir + startFilename)

    # Finds which parser is right for the file
    if(IDTypeNum < 9):
        tmpStr = parseDataReadPlayerTracking(tmpData)
    elif(IDTypeNum < 39):
        tmpStr = parseDataReadTotalStatistics(tmpData)

    writeFile(tmpStr, endFilename, 'w')
    return

# Download data from the web
def getNBAPlayerTrackDataFromWeb(urlStr, downloadedFilename):
    # Get data
    response = urllib.request.urlopen(urlStr)
    html = response.read()

    # Write html to a new file
    target = open(nbaFileDir + downloadedFilename, 'wb')
    target.write(html)
    target.close
    return

# Get the url of NBA Total Statistics
def getURLAddrTotalStat(seasonStr, teamID):
    urlAddrTotalStats = "http://stats.nba.com/stats/teamplayerdashboard?Season=" + seasonStr + "&SeasonType=Regular+Season&LeagueID=00&TeamID=" + teamID + "&MeasureType=Base&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope="
    return urlAddrTotalStats

# Append the header to the file
def appendTotalStatisticsIntoOneFile():
    tmpStr = '"GROUP_SET","PLAYER_ID","PLAYER_NAME","GP","W","L","W_PCT","MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","TOV","STL","BLK","BLKA","PF","PFD","PTS","PLUS_MINUS","DD2","TD3",\n'
    # Write file
    writeFile(tmpStr, totalStatFilename, 'a')
    return

# Combines all the Total Statistics files into one file
def combineTotalStatisticsIntoOneFile(inputFilename, count):
    tmpStr = openFile(nbaFileDir + inputFilename)

    # Insert next line after each file
    tmpStr += "\n"

    # Delete top row
    startPos = tmpStr.find('"Players"')
    endPos = tmpStr.__len__()
    tmpStr = tmpStr[startPos:endPos]

    # Write file
    writeFile(tmpStr, totalStatFilename, 'a')
    writeFile(tmpStr, totalStatFilename + "Copy", 'a')

    return

def main():
    # Delete "Total Statistics.csv" file first
    try:
        os.remove(nbaFileDir + totalStatFilename)
        os.remove(nbaFileDir + totalStatFilename + "Copy")
    except OSError:
        print("No file to delete")
        pass

    appendTotalStatisticsIntoOneFile()

    for x in range(0, 39):
# Get Player Tracking Statistics
        if x == 0:
            # Speed and Distance
            urlAddr = "http://stats.nba.com/js/data/sportvu/speedData.js"
            openFilename = "speedData.txt"
            saveFilename = "speedData.csv"
        elif x == 1:
            # Touch and Possession
            urlAddr = "http://stats.nba.com/js/data/sportvu/touchesData.js"
            openFilename = "touchesData.txt"
            saveFilename = "touchesData.csv"
        elif x == 2:
            # Passing
            urlAddr = "http://stats.nba.com/js/data/sportvu/passingData.js"
            openFilename = "passingData.txt"
            saveFilename = "passingData.csv"
        elif x == 3:
            # Defensive Impact
            urlAddr = "http://stats.nba.com/js/data/sportvu/defenseData.js"
            openFilename = "defenseData.txt"
            saveFilename = "defenseData.csv"
        elif x == 4:
            # Rebounding Opportunities
            urlAddr = "http://stats.nba.com/js/data/sportvu/reboundingData.js"
            openFilename = "reboundingData.txt"
            saveFilename = "reboundingData.csv"
        elif x == 5:
            # Drives
            urlAddr = "http://stats.nba.com/js/data/sportvu/drivesData.js"
            openFilename = "drivesData.txt"
            saveFilename = "drivesData.csv"
        elif x == 6:
            # Catch And Shoot
            urlAddr = "http://stats.nba.com/js/data/sportvu/catchShootData.js"
            openFilename = "catchShootData.txt"
            saveFilename = "catchShootData.csv"
        elif x == 7:
            # Pull Up
            urlAddr = "http://stats.nba.com/js/data/sportvu/pullUpShootData.js"
            openFilename = "pullUpShootData.txt"
            saveFilename = "pullUpShootData.csv"
        elif x == 8:
            # Shooting Efficiency
            urlAddr = "http://stats.nba.com/js/data/sportvu/shootingData.js"
            openFilename = "shootingData.txt"
            saveFilename = "shootingData.csv"
# Get Total Statistics 2013-14
        elif x == 9:
            # Atlanta Hawks
            seasonStr = "2013-14"
            teamName = "AtlantaHawks"
            teamID = "1610612737"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 10:
            # Boston Celtics
            seasonStr = "2013-14"
            teamName = "BostonCeltics"
            teamID = "1610612738"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 11:
            # Brooklyn Nets
            seasonStr = "2013-14"
            teamName = "BrooklynNets"
            teamID = "1610612751"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 12:
            # Charlotte Bobcats
            seasonStr = "2013-14"
            teamName = "CharlotteBobcats"
            teamID = "1610612766"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 13:
            # Chicago Bulls
            seasonStr = "2013-14"
            teamName = "ChicagoBulls"
            teamID = "1610612741"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 14:
            # Cleveland Cavaliers
            seasonStr = "2013-14"
            teamName = "ClevelandCavaliers"
            teamID = "1610612739"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 15:
            # Dallas Mavericks
            seasonStr = "2013-14"
            teamName = "DallasMavericks"
            teamID = "1610612742"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 16:
            # Denver Nuggets
            seasonStr = "2013-14"
            teamName = "DenverNuggets"
            teamID = "1610612743"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 17:
            # Detroit Pistons
            seasonStr = "2013-14"
            teamName = "DetroitPistons"
            teamID = "1610612765"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 18:
            # Golden State Warriors
            seasonStr = "2013-14"
            teamName = "GoldenStateWarriors"
            teamID = "1610612744"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 19:
            # Houston Rockets
            seasonStr = "2013-14"
            teamName = "HoustonRockets"
            teamID = "1610612745"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 20:
            # Indiana Pacers
            seasonStr = "2013-14"
            teamName = "IndianaPacers"
            teamID = "1610612754"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 21:
            # Los Angeles Clippers
            seasonStr = "2013-14"
            teamName = "LosAngelesClippers"
            teamID = "1610612746"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 22:
            # Los Angeles Lakers
            seasonStr = "2013-14"
            teamName = "LosAngelesLakers"
            teamID = "1610612747"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 23:
            # Memphis Grizzlies
            seasonStr = "2013-14"
            teamName = "MemphisGrizzlies"
            teamID = "1610612763"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 24:
            # Miami Heat
            seasonStr = "2013-14"
            teamName = "MiamiHeat"
            teamID = "1610612748"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 25:
            # Milwaukee Bucks
            seasonStr = "2013-14"
            teamName = "MilwaukeeBucks"
            teamID = "1610612749"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 26:
            # Minnesota Timberwolves
            seasonStr = "2013-14"
            teamName = "MinnesotaTimberwolves"
            teamID = "1610612750"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 27:
            # New Orleans Pelicans
            seasonStr = "2013-14"
            teamName = "NewOrleansPelicans"
            teamID = "1610612740"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 28:
            # New York Knicks
            seasonStr = "2013-14"
            teamName = "NewYorkKnicks"
            teamID = "1610612752"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 29:
            # Oklahoma City Thunder
            seasonStr = "2013-14"
            teamName = "OklahomaCityThunder"
            teamID = "1610612760"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 30:
            # Orlando Magic
            seasonStr = "2013-14"
            teamName = "OrlandoMagic"
            teamID = "1610612753"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 31:
            # Philadelphia 76ers
            seasonStr = "2013-14"
            teamName = "Philadelphia76ers"
            teamID = "1610612755"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 32:
            # Phoenix Suns
            seasonStr = "2013-14"
            teamName = "PhoenixSuns"
            teamID = "1610612756"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 33:
            # Portland Trail Blazers
            seasonStr = "2013-14"
            teamName = "PortlandTrailBlazers"
            teamID = "1610612757"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 34:
            # Sacramento Kings
            seasonStr = "2013-14"
            teamName = "SacramentoKings"
            teamID = "1610612758"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 35:
            # San Antonio Spurs
            seasonStr = "2013-14"
            teamName = "SanAntonioSpurs"
            teamID = "1610612759"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 36:
            # Toronto Raptors
            seasonStr = "2013-14"
            teamName = "TorontoRaptors"
            teamID = "1610612761"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 37:
            # Utah Jazz
            seasonStr = "2013-14"
            teamName = "UtahJazz"
            teamID = "1610612762"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"
        elif x == 38:
            # Washington Wizards
            seasonStr = "2013-14"
            teamName = "WashingtonWizards"
            teamID = "1610612764"
            urlAddr = getURLAddrTotalStat(seasonStr, teamID)
            openFilename = teamName+"TotalStatistics"+seasonStr+".txt"
            saveFilename = teamName+"TotalStatistics"+seasonStr+".csv"

        # Wait 5 seconds before download
        time.sleep(5)
        getNBAPlayerTrackDataFromWeb(urlAddr, openFilename)
        parseNBADataIntoCSV(openFilename, saveFilename, x)

        if x > 8:
            combineTotalStatisticsIntoOneFile(saveFilename, x)


        print("Reached end of function for " + saveFilename)


    return



main()





