# Plans

## initial meeting
#### what are we developing?
--> a program that shows the best combination of courses. 
**features of the program** --> 
- when user inputs the courses to take, our program shows the combination that works. It shows the number of combination that can be made with those 4 courses, which signifies the likeliness the user will grab all of those courses. (e.g. if one wants TUT101, CHM210, CSC207, PHI101 but there is only 1 combination that these 4 classes can be put together, it is less likely that the user gets all of them). 
- Also, the program will sort the combinations based on different criteria such as exclude certain time period, include/exclude the course taught by certain professor, etc.
- (NEW!) user can input more courses than the desired number to take --> e.g. user inputs all the desired courses (suppose 7), and wants to see what combinations (of 4 courses) are likely, it displays the combinations and the variations of time periods for each course combination.
- other features...

#### Technical part:
- **how?** we did not develop an exact algorithm yet, but we will use brute force method - that priorly computes every possibilities of courses and takes out what is needed. 
- **input format** the input format will be like TUT101 PHY132 etc.. if the user wants to specify certain course section, user can write PHY132-01 and the program will use this exact -01 section and not else.
we also need to think of the input format when user wants to exclude certain sections (of certain professors), exclude certain time period, and cases when user inputs more courses than 4 and wants to get combinations of 4, and when user wants course overload (taking 5 courses). 
- **we need database for course details** since we want user to just type 'PHI101', we need database for knowing the details of the course.
our data about courses will be organized into a nested list (2d list):

[[coursename, professor, course ID, day of week, start time, end time, alt day of week, alt start time, alt end time],
 [PHI111, Nyden, 00000, MWF, 3:00PM, 3:50PM, null, null, null]
 [MAT133, French, 00001, MWF, 1:00PM, 2:20PM, null, null, null]]
'alt start time' is for special courses that have unequal times during the week. (e.g. Tuesday 1:00PM-1:50PM + Thursday 3:00PM-5:00PM)
- **how will we program?** after coming up with the basics together somehow, we will implement features in different branches and merge them. we can work on the basics together in a google docs during zoom call or smth. it should be quick. First, lets get everyone set up with the environment.
- **Things to think about?** how to make this into a more appealing program to interact? should we make this into a website? should we just make it into command line program and distribute? let's find a way to make people want to use this, bcz not a lot of ppl like typing in a command line to get results.
