from database import allClasses
class Structure:
    def __init__(self, id, name, status, days, time, faculty, ifalt, secname,  index, tfad, haslab):
        self.id = id ##should be int
        self.name = name ##should be string
        self.status = status #should be in or boolean
        self.days = days # should be list of ints with the num 1 reprresenting Monday and the num 2 representing Teusday
        self.time = time ##should be hour * 60 + minutes

        self.faculty = faculty ## should be string
        self.ifalt = ifalt ##should be boolean or integer
        self.secname = secname ##should be string
        self.index = index
        self.times_forall_days = tfad
        self.haslab = haslab

class storage:
    def __init__(self, set, list):
        self.set = set
        self.list = list

def compare(class1, class2):
    if (class2.starttime >= class1.starttime and class2.starttime <= class1.endtime):
        return False
    else:
        return True
    
def time_print(time):
    return "" + time[0] + "-" + time[1]
def day_print(day):
    match day:
        case 0:
            return "M: "
        case 1:
            return "T: "
        case 2:
            return "W: "
        case 3:
            return "TH: "
        case 4:
            return "F:"
        
        

def print_output(struct):
    schedtemp = []
    temp = ""
    for i in range(len(struct)):
        classtemp = struct

        for i in allClasses.set:
            if (i.secname == struct):
                classtemp = i

        temp += struct + " "
        if (len(classtemp.time == 0)):
            temp += "No times have been established for this class"
        else:
            for i in range(5):
                if (i == 4):
                    temp += day_print(i) + time_print(classtemp.time[i])  
                temp += day_print(i) + time_print(classtemp.time[i]) + "; "
        schedtemp.append(temp)
    return schedtemp
    
    




