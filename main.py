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

all_comb_length = len(all_combinations)

### clustering all_combinations according to same course combinations but different time periods
### "comb_no_repeat" is all the combination of courses that can be made (not taking time periods into account)
### "comb_clusters" is the varying time sections that can be made corresponding to each course combination.
comb_no_repeat = []
comb_clusters = []

for combination in all_combinations_w_names:
    combination_nosection = [c[:7] for c in combination]
    for i, x in enumerate(comb_no_repeat):
        if set(x) == set(combination_nosection):
            comb_clusters[i].append(combination)
            break
    else:
        comb_no_repeat.append(set(combination_nosection))
        comb_clusters.append([combination])


print(f"there are {all_comb_length} combinations of {userinput_comblength} courses overall.")
print(f"there are {len(comb_no_repeat)} course combinations that can be made:")
for i in range(len(comb_no_repeat)):
    comb = " ".join(comb_no_repeat[i])
    print(f"({i}): {comb} -> {len(comb_clusters[i])} different time period combinations")

