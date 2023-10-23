class Structure:
    def __init__(self, id, name, status, days, starttime, endtime, faculty, ifalt, altdays, alttimes, index):
        self.id = id ##should be int
        self.name = name ##should be string
        self.status = status #should be in or boolean
        self.days = days # should be list of ints with the num 1 reprresenting Monday and the num 2 representing Teusday
        self.starttime = starttime ##should be hour * 60 + minutes
        self.endtime = endtime ##should be hour * 60 + minutes
        self.faculty = faculty ## should be string
        self.ifalt = ifalt ##should be boolean or integer
        self.altdays = altdays #should be list of ints like days, only with stuff if altdays is true
        self.alttimes = alttimes #list of start times and endtimes with index 0 representing the start and endtimes of altday at index 0
        self.index = index
        self.selfDict = [[self.id, self.name, self.index],  [self.status, self.days, self.starttime, self.endtime, self.faculty, self.ifalt, self.altdays, self.alttimes]]
    


class storage:
    def __init__(self, set, list):
        self.set = set
        self.list = list

def compare(class1, class2):
    if (class2.starttime >= class1.starttime and class2.starttime <= class1.endtime):
        return False
    else:
        return True

