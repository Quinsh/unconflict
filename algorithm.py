import sys

### this function finds all the possible combinations without time conflict.
### it's implemented with recursive method + backtracking
def generate_combinations(courses, current_combination=[]):
    if len(current_combination) == 4:
        return [current_combination.copy()]

    if not courses:
        return []

    current_course = courses[0]
    remaining_courses = courses[1:]

    # Exclude the current course
    combinations_without_current = generate_combinations(
        remaining_courses, current_combination)

    # Include the current course if it doesn't conflict
    combinations_with_current = []
    if not conflicts_with_any(current_course, current_combination):
        combinations_with_current = generate_combinations(
            remaining_courses, current_combination + [current_course])

    return combinations_without_current + combinations_with_current

def conflicts_with_any(course, course_list):
    for c in course_list:
        if conflicts(course, c):
            return True
    return False

def conflicts(course1, course2):
    # Check if any time slot of course1 conflicts with any time slot of course2
    pass # erase this line later

# just testing
# print(generate_combinations(["TUT101", "PHY132", "CHM210", "PHI111", "MAT215"], []))
