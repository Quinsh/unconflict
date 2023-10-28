import csv
import datetime

from Structure import Structure
from Structure import storage

from collections import Counter

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

        start_time = datetime.datetime.strptime(start_time_str, '%I:%M %p').time()
        end_time = datetime.datetime.strptime(end_time_str, '%I:%M %p').time()

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

def find_w_name(coursename):
    for course in tempset:
        if course.secname == coursename:
            return course
    
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

def checkfreq(comb_clust):
    classtuple = tuple(comb_clust)

    templist = [item for lst in classtuple for item in lst]
    var_freq = Counter(templist)



    most_common_variable = var_freq.most_common(1)
    second_most_common_variable = var_freq.most_common(2)

    tempstring = "<p>2 most common sections: <i id='occurence'>" + \
        most_common_variable[0][0] + "</i> and <i id='occurence'>" + \
        second_most_common_variable[1][0] + "</i> <br></p>"

    return tempstring


def return2freq(comb_clust):
    classtuple = tuple(comb_clust)

    templist = [item for lst in classtuple for item in lst]
    var_freq = Counter(templist)

    most_common_variable = var_freq.most_common(1)
    second_most_common_variable = var_freq.most_common(2)

    returnvalue = [most_common_variable[0][0],
                   second_most_common_variable[1][0]]
    return returnvalue


def time_print(time):
    tempstart =  time[0].strftime("%H:%M")
    tempend = time[1].strftime("%H:%M")
    return "" + tempstart + "-" + tempend
def day_print(day):
    match day:
        case 1:
            return "M"
        case 2:
            return "T"
        case 3:
            return "W"
        case 4:
            return "TH"
        case 5:
            return "F"



def print_output(struct):
    schedtemp = []
    temp = ""

    for i, coursename in enumerate(struct):
        classtemp = Structure(0, "", 0, [], [], "", 0, "", 0, [], False)

        for j in allClasses.set:

            if (j.secname == coursename):
                classtemp = j


        temp = "<p>"
        temp += classtemp.secname[:7] + " "

        if (len(classtemp.time) == 0):
            temp += "No times have been established for this class<br></p>"
            schedtemp.append(temp)
            continue
        else:

            for d in range(len(classtemp.days)):
                k = 0
                for m in classtemp.days[d]:

                    if (d > 0):
                        temp += classtemp.secname[:7] + "L "
                    if k == len(classtemp.days[d]) - 1:
                        temp += day_print(m) + ": "
                    else:
                        temp += day_print(m)
                        k += 1
                if d == len(classtemp.days) - 1:
                    temp += time_print(classtemp.time[d][:5]) + ";<br></p>"
                else:
                    temp += time_print(classtemp.time[d]) + ";<br>"

        schedtemp.append(temp)
    return schedtemp

def print_outputday(struct):
    coursetemp = ["<p>M:", "T:", "W:", "TH:", "F:"]
    schedtemp = []

    for i, coursename in enumerate(struct):

        for j in allClasses.set:

            if (j.secname == coursename):

                schedtemp.append(j)



    for schedcourse in range(len(schedtemp)):
        for d in range(5):
            if schedtemp[schedcourse].times_forall_days[d] != []:

                coursetemp[d] += " " + time_print(schedtemp[schedcourse].times_forall_days[d][0])
        if schedcourse == len(schedtemp) - 1:
            coursetemp[4] += ";<br></p>"


    return coursetemp[0] + coursetemp[1] + coursetemp[2] + coursetemp[3] + coursetemp[4]

def is_time_in_range(start_time, check_time, end_time):
    return start_time <= check_time <= end_time

def timegraph_helper(timesforalldays_combined):
    courseexists = "XXXXXXXXX"
    coursedoesnot = "         "
    text = "<pre>      |    MON    |    TUE    |    WED    |    THU    |    FRI    " + "<br>"
    current_time = datetime.time(8, 0)
    end_time = datetime.time(21, 0)
    interval_minutes = 20

    while current_time <= end_time:
        text += current_time.strftime("%H:%M") + " "
        
        for days in timesforalldays_combined:
            if not days:
                text += "| " + coursedoesnot + " "
            else:
                for timetuples in days:
                    if is_time_in_range(timetuples[0], current_time, timetuples[1]):
                        text += "| " + courseexists + " "
                        break
                else:
                    text += "| " + coursedoesnot + " "
        text += " <br>"
        
        # Convert time to datetime to perform arithmetic operations
        datetime_combined = datetime.datetime.combine(datetime.date.today(), current_time)
        datetime_combined += datetime.timedelta(minutes=interval_minutes)
        # Extract the time part again
        current_time = datetime_combined.time()
    
    text += "</pre>"
    
    return text
    

def timegraph(listofcourses):
    timeforalldays_combined = [[],[],[],[],[]]
    for coursename in listofcourses:
        course = find_w_name(coursename)
        for i, times_each_day in enumerate(course.times_forall_days):
            timeforalldays_combined[i] += times_each_day
                
    return timegraph_helper(timeforalldays_combined)
    
    

""" for testing:
courselist = allClasses.list

for n in range(95, 105):
    print(courselist[n].secname, courselist[n].haslab)
"""
