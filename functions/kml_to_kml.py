import xml.etree.ElementTree as ET
from datetime import datetime

StartTime = datetime.now()
Tree = ET.parse('../Metro_CDMX.kml')
root = Tree.getroot()
OutFileName = "Metro_CDMX.csv"
f = open(OutFileName, "w")
f.write('bottle_id, time, lat, lon' + '\n')

TotalLineCounter = 0

for line in root.iter('*'):
    if line.tag == '{http://www.opengis.net/kml/2.2}description':
        TotalLineCounter += 1
        FullString = line.text
        BottleName = FullString.split('<b>')[1]
        BottleName = BottleName[18:27]
        BottleTime = FullString.split('<b>')[2]
        BottleTime = BottleTime[18:37]
        BottleYear = str(BottleTime[0:4])
        BottleMonth = str(BottleTime[5:7])
        BottleDay = str(BottleTime[8:10])
        BottleHour = str(BottleTime[11:13])
        BottleMinute = str(BottleTime[14:16])
        BottleSecond = str(BottleTime[17:19])
        BottleDayStamp = BottleYear + '-' + BottleMonth + '-' + BottleDay
        BottleTimeStamp = 'T' + BottleHour + ':' + BottleMinute + ':' + BottleSecond
        BottleCoordinates = FullString.split('<b>')[3]
        BottleLon, BottleLat = BottleCoordinates.split(',')
        BottleLat = BottleLat[:-4]
        BottleLon = BottleLon[14:]
        BottleLine = BottleName + ',' + BottleDayStamp + BottleTimeStamp + ',' + BottleLat + ',' + BottleLon
        f.write(BottleLine + '\n')

f.close()

print(TotalLineCounter)
EndTime = datetime.now()
print("Done in: " + str(EndTime - StartTime))