import sys

from database import allClasses

courselist = allClasses.list
courseset = allClasses.set

### given user inputs ['CHM-129', 'PHY-132']
### make list of Structure objects of the courses above with all different time periods
def possible_courses(userinputs):
    temp_li = []
    for course in courseset:
        for usercourse in userinputs:
            if course.secname[:7] == usercourse:
                temp_li.append(course)
    return temp_li

### returns the list of structure object that has the coursename (should be inputted like "PHY-132-" including the last '-' or like "PHY-132L")
def findall_w_name(coursename):
    li = []
    for course in courseset:
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
    times_forall_days1 = course1.times_forall_days
    times_forall_days2 = course2.times_forall_days
    
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

print(courselist[97].secname, courselist[97].times_forall_days)
print(courselist[120].secname, courselist[120].times_forall_days)

print(conflicts(courselist[97], courselist[120]))

combinations = generate_combinations(possible_courses(["CHM-129", "PHY-132", "CSC-161", "MAT-215", "PHI-111"]))

for i, c in enumerate(combinations):
    c = [b.secname for b in c]
    combinations[i] = c
    
print(combinations)

"""