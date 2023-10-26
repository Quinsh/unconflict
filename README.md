# unconflict
Unconflict aims to help Grinnell College students with the best combination of courses for registration. Made with fellow CS freshmen at Grinnell.

## use
anyone can use freely. For experience go to http://www.unconflictgrinnell.com/

## project details
we use brute force method to come up with different course schedules and sort out the best based on diverse criteria.

## Responsibles
Gun Woo Kim (closhu) | Samuel Grayson (doc4science) | Rhys Howell (Howell45)

## Log
In October 11, we come up with a fun idea to compute best fit course schedules in order to ease students' life in Grinnell. However, the actual development is postponed until October 23, when we realize it can't be delayed more.

GunWoo designs recursive backtracking approach to generate every possible course combinations with no time conflicts. Then, Samuel proposes to display them according to user preference, including or excluding certain sections. To see if two courses conflict in their time, a specific data structure has to be made. This is handled by Rhys, who works on the data designing side. Rhys also works on developing some features of the program with GunWoo. Finally, Samuel makes the initial python program to be a webside using Flask. The website is revised by GunWoo, who adds css styling to it.
