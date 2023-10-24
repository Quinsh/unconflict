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
    

def make_timesforalldays(days, time):
    times_forall_days = [[],[],[],[],[]]
    for i, daylist in enumerate(days):
        for day in daylist:
            times_forall_days[day-1] = [time[i]]
    return times_forall_days

def exists(secname, courseset):
    for course in courseset:
        if course.secname[:8] == secname:
            return True
    return False

def make_haslab(secname, courseset):
    if secname[7:8] == '-' and exists(secname[:7]+'L', courseset):
        return True
    else:
        return False

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
    timetemp = maketime(rows[i][5])
    daystemp = makedays(rows[i][4])
    secname = rows[i][2]
    
    temp = Structure(makeInt(rows[i][0]), rows[i][3], makestatus(rows[i][1]), daystemp, 
                    timetemp, rows[i][6], makeifalt(rows[i][5]), secname, i - 1, 
                    make_timesforalldays(daystemp, timetemp), False)
    
    templist.append(temp)

tempset = set(templist)

for i in range(len(templist)):
    templist[i].haslab = make_haslab(templist[i].secname, tempset)

def findall_w_name(coursename):
    li = []
    for course in tempset:
        if course.secname[:8] == coursename:
            li.append(course)
    return li

# making a joint course for courses that have labs
originalcourses = set()
for course in templist:
    if course.haslab:
        labs = findall_w_name(course.secname[:7] + 'L')
        for lab in labs:
            jointdays = course.days + lab.days
            jointtime = course.time + lab.time
            joint_timesforalldays = [course.times_forall_days[i] + lab.times_forall_days[i] for i in range(5)]
            newcourse = Structure(str(course.id) + " " + str(lab.id),
                                course.name + 'LAB', 
                                course.status, 
                                jointdays,
                                jointtime,
                                course.faculty + " " + lab.faculty,
                                course.ifalt + lab.ifalt, 
                                course.secname + '+' + lab.secname[7:],
                                0,
                                joint_timesforalldays,
                                False)
            templist.append(newcourse)
            originalcourses.add(lab)
        
        # remove the original course
        originalcourses.add(course)

for c in originalcourses:
    templist.remove(c)

tempset = set(templist)

allClasses = storage(tempset, templist)

""" for testing: 
courselist = allClasses.list

for n in range(95, 105):
    print(courselist[n].secname, courselist[n].haslab)
"""




