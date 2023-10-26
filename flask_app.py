#acknowledgement: giles, pythonanywhere
from flask import Flask, request

from processing import solution
from database import print_output

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        course_input = None
        combination_input = None
        include_input = None
        exclude_input = None
        course_input = request.form["course_input"]
        combination_input = request.form["combination_input"]
        include_input = request.form["include_input"]
        exclude_input = request.form["exclude_input"]

        returnlist = solution(course_input, combination_input, include_input, exclude_input)
        allcomblength = returnlist[0]
        comb_no_repeat = returnlist[1]
        comb_clusters = returnlist[2]

        formattedblocks = ""
        for i in range(len(comb_no_repeat)):
            temp = '''<div class="blocks">
                            <p class="block-title">'''
            temp += " ".join(comb_no_repeat[i])
            temp += '''</p>
                            <ul>'''
            for j, course in enumerate(comb_clusters[i]):
                temp += "<li>"
                temp += " ".join(course)
     ##  FOR TIMES       # temp += "</li></li>"
     ##  FOR TIMES       # temp += " ".join(print_output(course))
                temp += "</li>"
            temp += '''</ul>
                        </div>'''
            formattedblocks += temp

        return '''
            <html>
            <link rel="shortcut icon" href="/static/favicon.ico">
            <head>
                <link rel="stylesheet" href="/static/style.css">
            </head>

            <body>
                <div id="div-outermost">
                    <div id="space_above"></div>
                    <div id="div-flex">
                        <h1 id="combtitle"><i class="highlight">{totalsch}</i> total schedules!</h1>
                        <p class="titledesc">and <i class="highlight2">{coursecomb}</i> course combinations...</p>

                        {blocks}

                        <p><a href="/">Click here to make a new schedule</a>
                    </div>
                </div>
            </body>

            </html>
        '''.format(totalsch=allcomblength, coursecomb=len(comb_no_repeat), blocks=formattedblocks)

    return '''
    <html>
    <link rel="shortcut icon" href="/static/favicon.ico">
    <head>
        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>
        {errors}
        <div id="div-outermost">
            <div id="space_above"></div>
            <div id="div-flex">
                <h1><i class="highlight">UN</i>CONFLICT</h1>
                <p id="subtitle">course combinations at Grinnell</p>
                <form method="post" action=".">
                    <p class="ins">Desired Classes</p>
                    <div class="form__group">
                        <input name="course_input" class="form__input" placeholder="CSC-151 PHI-111 MAT-215" required=""/>
                    </div>

                    <p class="ins">Number of Classes in Schedule</p>
                    <div class="form__group">
                        <p><input name="combination_input" class="form__input" placeholder="4"/></p>
                    </div>


                    <p class="ins">Must Include Sections</p>
                    <div class="form__group">
                        <p><input name="include_input" class="form__input" placeholder="CSC-151-01"/></p>
                    </div>

                    <p class="ins">Must Exclude Sections</p>
                    <div class="form__group">
                        <p><input name="exclude_input" class="form__input" placeholder="MAT-215-05"/></p>
                    </div>

                    <p><input id="submitbutton" type="submit" value="MAKE SCHEDULE"/></p>
                    <br>
                    <br>
                    <p>Developed by CS Students at Grinnell College</p>
                    <a href="/aboutus">About Us</a>
                </form>
            </div>
        </div>
    </body>

    </html>
    '''.format(errors=errors)

@app.route("/aboutus", methods=["GET", "POST"])
def aboutus_page():
    return '''
       <html>
        <link rel="shortcut icon" href="/static/favicon.ico">
        <head>
            <link rel="stylesheet" href="/static/style.css">
        </head>

        <body>
            <div id="div-outermost">
                <p><a href="/">Click here to go home</a>
                <div id="space_above"></div>
                <div id="div-flex">
                    <p class="aboutus_st">developed by</p>
                    <p class="aboutus_names"><i id="gunwoo">Gun Woo Kim</i> | <i id="sam">Samuel Grayson</i> | <i id="rhys">Rhys Howell</i></p>
                    <p class="aboutus_desc"><i id="gunwoo">(algorithm dev)</i> | <i id="sam">(web development)</i> | <i id="rhys">(data
                            structure dev)</i></p>
                    <p class="aboutus_slight">CS freshmen as of 2023 :)</p>
                    <p class="aboutus_st">github repo</p>
                    <p class="aboutus_p">https://github.com/closhu/unconflict</p>
                    <p class="aboutus_st">contacts</p>
                    <p class="aboutus_p">kimgunwo@grinnell.edu<br>graysons@grinnell.edu<br>howellrh@grinnell.edu</p>
                    <p class="aboutus_st">about the project</p>
                    <br>
                    <div id="aboutproject">
                        <img src="/static/us2.png" width="100%"><br><br>
                        In October 11, we come up with a fun idea to compute best fit course schedules in order to ease students' life in Grinnell.
                        However, the actual development is postponed until October 23, when we realize it can't be delayed more.
                        <br><br>
                        GunWoo designs recursive backtracking approach to generate every possible course combinations with no time conflicts.
                        Then, Samuel proposes to display them according to user preference, including or excluding certain sections.
                        To see if two courses conflict in their time, a specific data structure has to be made.
                        This is handled by Rhys, who works on the data designing side. Rhys also works on developing some features of the program with GunWoo.
                        Finally, Samuel makes the initial python program to be a webside using Flask. The website is revised by GunWoo, who adds css styling to it.
                    </div>
                    <br>

                </div>
            </div>
        </body>

        </html>
    '''
