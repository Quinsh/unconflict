import csv
from datetime import datetime

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
    temp = days.split()

    rdays = []
    for i in range(0, len(temp)):
        middays = []
        if "TH" in temp[i]:
            middays.append(4)
            d = temp[i].replace("TH", '')
            temp[i] = d
        if "M" in temp[i]:
            middays.append(1)
            d = temp[i].replace("M", "")
            temp[i] = d
        if "T" in temp[i]:
            middays.append(2)
            d = temp[i].replace("T", "")
            temp[i] = d
        if "W" in temp[i]:
            middays.append(3)
            d = temp[i].replace("W", "")
            temp[i] = d
        if "F" in temp[i]:
            middays.append(5)
            d = temp[i].replace("F", "")
            temp[i] = d
        rdays.append(middays)
    rdays.sort()
    return rdays


def maketime(time):
    if time == "":
        return []
    time_list = time.split()
    while '-' in time_list:
        time_list.remove('-')
    fulltime = []

    for i in range(0, len(time_list), 4):
        start_time_str = f"{time_list[i]} {time_list[i + 1]}"
        end_time_str = f"{time_list[i + 2]} {time_list[i + 3]}"

        start_time = datetime.strptime(start_time_str, '%I:%M %p').time()
        end_time = datetime.strptime(end_time_str, '%I:%M %p').time()

        fulltime.append((start_time, end_time))

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
    temp = Structure(makeInt(rows[i][0]), rows[i][3], makestatus(rows[i][1]), makedays(rows[i][4]), maketime(rows[i][5]), rows[i][6], makeifalt(rows[i][5]), rows[i][2], i - 1)
    tempset.add(temp)
    templist.append(temp)

allClasses = storage(tempset, templist)




