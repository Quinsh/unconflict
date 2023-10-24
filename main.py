import sys

import algorithm

userinput_courses = list(sys.stdin.readline().rstrip().split())
userinput_comblength = int(sys.stdin.readline())

# combinations (with Structures)
all_combinations = algorithm.generate_combinations(algorithm.possible_courses(userinput_courses), 
                                                    userinput_comblength)

# convert Structures into names
all_combinations_w_names = []
for combination in all_combinations:
    temp = [course.secname for course in combination]
    all_combinations_w_names.append(temp)

print(all_combinations_w_names)