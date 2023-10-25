
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
    
    
    




