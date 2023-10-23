import csv

from Structure import Structure
from Structure import storage

def makeInt(num):
    return int(num)

def makestatus(status):
    if (status.__eq__("Active")):
        return 1
    else:
        return 0
def makedays(days):
    rdays = []
    if "TH" in days:
        rdays.append(4)
        days.replace("TH", "")
    if "M" in days:
        rdays.append(1)
        days.replace("M", "")
    if "T" in days:
        rdays.append(2)
        days.replace("T", "")
    if "W" in days:
        rdays.append(3)
        days.replace("W", "")
    if "F" in days:
        rdays.append(5)
        days.replace("F", "")
    rdays.sort()
    return rdays


def maketime(time):
    if time == "":
        return []
    fulltime = []
    if len(time) == 20:
        start = time[0:7:1]
        end = time[11:18]
        tempstart = (int(start[:1]) * 60) + (int(start[2:4]))
        tempend = (int(end[:1]) * 60) + (int(end[2:4]))

        if "AM" not in start:
            tempstart += 720
        if "AM" not in end:
            tempend += 720
        fulltime.append(tempstart)
        fulltime.append(tempend)
        return fulltime
    elif len(time) == 21:
        start = time[0:8:1]
        end = time[11: 19:1]
        tempstart = (int(start[:1]) * 60) + (int(start[3:5]))
        tempend = (int(end[:1]) * 60) + (int(end[3:5]))
        if "AM" not in start:
            tempstart += 720
        if "AM" not in end:
            tempend += 720
        fulltime.append(tempstart)
        fulltime.append(tempend)
        return fulltime
    elif len(time) == 37:
        startone = time[0:7:1]
        endone = time[11:18:1]
        starttwo = time[19:26:1]
        endtwo = time[30:38:1]

        tempstartone = (int(startone[:1]) * 60) + (int(startone[2:4]))
        tempendone = (int(endone[:1]) * 60) + (int(endone[2:4]))
        if "AM" not in startone:
            tempstartone += 720
        if "AM" not in endone:
            tempendone += 720
        tempstarttwo = (int(starttwo[:1]) * 60) + (int(starttwo[2:4]))
        tempendtwo = (int(endtwo[:1]) * 60) + (int(endtwo[2:4]))
        if "AM" not in starttwo:
            tempstarttwo += 720
        if "AM" not in endtwo:
            tempendtwo += 720
        temp = [tempstartone, tempendone]
        temptwo = [tempstarttwo, tempendtwo]
        fulltime.append(temp)
        fulltime.append(temptwo)
        return fulltime
    elif len(time) == 39:
        startone = time[0:8:1]
        endone = time[11: 19:1]
        tempstartone = (int(startone[:1]) * 60) + (int(startone[3:5]))
        tempendone = (int(endone[:1]) * 60) + (int(endone[3:5]))
        starttwo = time[20:28:1]
        endtwo = time[31:38:1]
        tempstarttwo = (int(starttwo[0:1]) * 60) + (int(starttwo[3:5]))
        tempendtwo = (int(endtwo[:1]) * 60) + (int(endtwo[3:5]))
        if "AM" not in startone:
            tempstartone += 720
        if "AM" not in endone:
            tempendone += 720
        if "AM" not in starttwo:
            tempstarttwo += 720
        if "AM" not in endtwo:
            tempendtwo += 720
        temp = [tempstartone, tempendone]
        temptwo = [tempstarttwo, tempendtwo]
        fulltime.append(temp)
        fulltime.append(temptwo)
        return fulltime
    else:
        startone = time[0:7:1]
        endone = time[11: 18:1]
        tempstartone = (int(startone[:1]) * 60) + (int(startone[2:4]))
        tempendone = (int(endone[:1]) * 60) + (int(endone[2:4]))
        starttwo = time[19:27:1]
        endtwo = time[30:38:1]
        tempstarttwo = (int(starttwo[0:1]) * 60) + (int(starttwo[3:5]))
        tempendtwo = (int(endtwo[:1]) * 60) + (int(endtwo[3:5]))
        if "AM" not in startone:
            tempstartone += 720
        if "AM" not in endone:
            tempendone += 720
        if "AM" not in starttwo:
            tempstarttwo += 720
        if "AM" not in endtwo:
            tempendtwo += 720
        temp = [tempstartone, tempendone]
        temptwo = [tempstarttwo, tempendtwo]
        fulltime.append(temp)
        fulltime.append(temptwo)
        return fulltime

def makeifalt(times):
    if len(times) > 36 and len(times) < 40:
        return 1
    else:
        return 0



filename = "Course_Offering_0007 (1).csv"
tempset = set()
templist = []
# initializing the titles and rows list

rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row


    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for i in range(1, len(rows) - 1):
    temp = Structure(makeInt(rows[i][0]), rows[i][3], makestatus(rows[i][1]), makedays(rows[i][4]), maketime(rows[i][5]), rows[i][6], makeifalt(rows[i][5]), i - 1)
    tempset.add(temp)
    templist.append(temp)

allClasses = storage(tempset, templist)


