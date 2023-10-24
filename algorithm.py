import sys

from database import allClasses

courselist = allClasses.list

### given user inputs ['CHM-129', 'PHY-132']
### make list of Structure objects of the courses above with all different time periods
def possible_courses(userinputs):
    temp_li = []
    for course in courselist:
        for usercourse in userinputs:
            if course.secname[:8] == usercourse+'-': # there is reason why I compare like this. It's bcz some courses are like 'CHM-129L' (lab) and we wanna exclude it.
                temp_li.append(course)
    return temp_li

### returns the list of structure object that has the coursename (should be inputted like "PHY-132-" including the last '-' or like "PHY-132L")
def findall_w_name(coursename):
    li = []
    for course in courselist:
        if course.secname[:8] == coursename:
            li.append(course)
    return li

### this function finds all the possible combinations without time conflict.
### it's implemented with recursive method + backtracking
def generate_combinations(courses, lengthofcomb, current_combination=[]):
    if len(current_combination) == lengthofcomb:
        return [current_combination.copy()]

    if not courses:
        return []

    current_course = courses[0]
    remaining_courses = courses[1:]

    # Exclude the current course
    combinations_without_current = generate_combinations(
        remaining_courses, lengthofcomb, current_combination)

    # Include the current course if it doesn't conflict
    combinations_with_current = []
    if not conflicts_with_any(current_course, current_combination):
        combinations_with_current = generate_combinations(
            remaining_courses, lengthofcomb, current_combination + [current_course])

    return combinations_without_current + combinations_with_current

def conflicts_with_any(course, course_list):
    for c in course_list:
        if conflicts(course, c):
            return True
    return False


def conflicts(course1, course2):
    # check if course1 and course2 are same (ex: CSC-151-01 ad CSC-151-02)
    if course1.secname[:7] == course2.secname[:7]:
        return True
    
    # check if time conflicts for any day of week
    # for this, we make times_forall_days1 
    times_forall_days1 = [[], [], [], [], []] # each index represents monday, tues, wed, ..
    times_forall_days2 = [[], [], [], [], []] # each index should be a list of (starttime, endtime) or just 
    
    for i, daylist in enumerate(course1.days):
        for day in daylist:
            times_forall_days1[day-1] = [course1.time[i]]
    for i, daylist in enumerate(course2.days):
        for day in daylist:
            times_forall_days2[day-1] = [course2.time[i]]
    
    # add lab times, for example: CHM-129-01 and CHM-129L-01 are joint
    course1_labs = findall_w_name(course1.secname[:7]+'L')
    if course1_labs:
        for course1_lab in course1_labs:
            for i, daylist in enumerate(course1_lab.days):
                for day in daylist:
                    if times_forall_days1[day-1]:
                        times_forall_days1[day-1].append(course1_lab.time[i])  
                    else:
                        times_forall_days1[day-1] = [course1_lab.time[i]]
    course2_labs = findall_w_name(course2.secname[:7]+'L')
    if course2_labs:
        for course2_lab in course2_labs:
            for i, daylist in enumerate(course2_lab.days):
                for day in daylist:
                    if times_forall_days2[day-1]:
                        times_forall_days2[day-1].append(course2_lab.time[i])
                    else:
                        times_forall_days2[day-1] = [course2_lab.time[i]]
    
    # ERASE THIS LATER: print(times_forall_days1, "\n\n" , times_forall_days2)
    
    # now compare if times_forall_days1 and times_forall_days2 conflict...
    for i in range(5):
        for timeset1 in times_forall_days1[i]:
            for timeset2 in times_forall_days2[i]:
                if timeset1[0] > timeset2[1] or timeset2[0] > timeset1[1]:
                    pass
                else:
                    return True
                
    return False



### BELOW JUST FOR TESTING
"""
print(courselist[97].secname, courselist[97].days)
print(courselist[187].secname, courselist[185].days)

print(conflicts(courselist[97], courselist[185]))

combinations = generate_combinations(possible_courses(["CHM-129", "PHY-132", "CSC-161", "MAT-215", "PHI-111"]))

for i, c in enumerate(combinations):
    c = [b.secname for b in c]
    combinations[i] = c
    
print(combinations)

"""