
nbaFileDir = "C:/Users/glau/Downloads/nbaSpreadsheets/"

# Open downloaded file
def openFile(filename):
    with open(filename) as myfile:
        data = myfile.read()
        myfile.close()
    return data

# Write parsed string into a new file
def writeFile(dataStr, filename):
    # Write dataStr to a new file
    target = open(nbaFileDir + filename, 'w')
    target.write(dataStr)
    target.close
    return

def main():
    tmpData = openFile(nbaFileDir + "shootingData.csv")
    writeFile(tmpData, "shootingDataModified.xls")
    return

main()