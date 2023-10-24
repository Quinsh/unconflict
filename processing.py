import algorithm

def solution(course_input, combination_input):
    userinput_courses = list(course_input.rstrip().split())
    userinput_comblength = int(combination_input)
    all_combinations = algorithm.generate_combinations(algorithm.possible_courses(userinput_courses),
                                                   userinput_comblength)
    all_combinations_w_names = []
    for combination in all_combinations:
        temp = [course.secname for course in combination]
        all_combinations_w_names.append(temp)
    return all_combinations_w_names