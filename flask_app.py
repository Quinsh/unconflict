#acknowledgement: giles, pythonanywhere
from flask import Flask, request

from processing import solution
from database import print_output
from database import checkfreq
from database import return2freq
from database import timegraph

app = Flask(__name__)
app.config["DEBUG"] = True

course_input = None
combination_input = None
include_input = None
exclude_input = None
returnlist = []
allcomblength = None
comb_no_repeat = None
comb_clusters = None

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    global course_input
    global combination_input
    global include_input
    global exclude_input
    global returnlist
    global allcomblength
    global comb_no_repeat
    global comb_clusters
    if request.method == "POST":
        course_input = request.form["course_input"].upper()
        try:
            combination_input = float(request.form["combination_input"])
        except:
             errors += "<p>Please enter a number in Number of Classes in Schedule</p>\n".format(request.form["combination_input"])
        include_input = request.form["include_input"].upper()
        exclude_input = request.form["exclude_input"].upper()

        if errors == "":
            returnlist = solution(course_input, combination_input, include_input, exclude_input)

            allcomblength = returnlist[0]
            comb_no_repeat = returnlist[1]
            comb_clusters = returnlist[2]

            formattedblocks = ""
            for i in range(len(comb_no_repeat)):
                temp = '''<div class="blocks">
                                <p class="block-title">'''
                temp += " ".join(comb_no_repeat[i])
                temp += '''</p>'''

                # "most frequent 2 courses are ... "
                temp += checkfreq(comb_clusters[i])

                # list of courses displayed
                temp += "<ul>"
                for j, course in enumerate(comb_clusters[i]):
                    temp += "<li>"
                    mostcommoncourses = return2freq(comb_clusters[i])
                    coursestring = ""
                    for c in course:
                        if c == mostcommoncourses[0] or c == mostcommoncourses[1]:
                            coursestring += "<i id='commoncourse'>" +  c + " </i>"
                        else:
                            coursestring += c + " "

                    temp += f"<p><a id='linktime' href='/time?var1={' '.join(course)}'>" + coursestring + "</a>"
                  ###  temp += "</li></li>"
                   ### temp += "     ".join(print_output(course))
                    temp += "</li>"
                temp += "</li></li>"
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
        else:
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
                            <p class="ins">Desired Classes <i id="smallins">(can be more than 4, should be separated by space)</i> <span class="info-button">
                    <span class="info-icon"></span>
                    <span class="info-content">
                      Enter a list of classes that you are interested in taking. Each class should be entered in the following format "AAA-### BBB-###". For example, one might enter "CSC-161 RUS-222 PHY-132 SOC-104 HIS-100 CHM-210" There is no limit to the number of classes entered.
                    </span>
                  </span></p>
                            <div class="form__group">
                                <input name="course_input" class="form__input" placeholder="CSC-151 PHI-111 MAT-215" required=""/>
                             </div>
                            <p class="ins">Number of Classes in Schedule
                            <span class="info-button">
                             <span class="info-icon"></span>
                              <span class="info-content">
                                 Enter the number of classes that you want in your schedule. For instance enter "4" if you want to take four classes. This number must be less than the number of courses entered in the above field.
                             </span>
                            </span></p>
                            <div class="form__group">
                                <p><input name="combination_input" class="form__input" placeholder="4" required=""/></p>
                            </div>


                            <p class="ins">Must Include Sections
                            <span class="info-button">
                             <span class="info-icon"></span>
                            <span class="info-content">
                              Enter specific section numbers that you want included in your schedule. For example, type "CSC-161-01" if you only want schedules with the 1st section of CSC-161 included.
                             </span>
                           </span></p>
                            <div class="form__group">
                                <p><input name="include_input" class="form__input" placeholder="CSC-151-01 MAT-215-03"/></p>
                            </div>

                            <p class="ins">Must Exclude Sections
                            <span class="info-button">
                            <span class="info-icon"></span>
                              <span class="info-content">
                                Enter specific section numbers that you do not want included in your schedule. For example, type "CSC-161-01" if you want to take CSC-161, but not the 1st section.
                              </span>
                            </span></p>
                            <div class="form__group">
                                <p><input name="exclude_input" class="form__input" placeholder="PHI-111-01"/></p>
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
                    <p class="ins">Desired Classes <i id="smallins">(can be more than 4, should be separated by space)</i>
                    <span class="info-button">
                    <span class="info-icon"></span>
                    <span class="info-content">
                      Enter a list of classes that you are interested in taking. Each class should be entered in the following format "AAA-### BBB-###". For example, one might enter "CSC-161 RUS-222 PHY-132 SOC-104 HIS-100 CHM-210" There is no limit to the number of classes entered.
                    </span>
                  </span></p>
                    <div class="form__group">
                        <input name="course_input" class="form__input" placeholder="CSC-151 PHI-111 MAT-215" required=""/>
                    </div>

                    <p class="ins">Number of Classes in Schedule
                    <span class="info-button">
                    <span class="info-icon"></span>
                    <span class="info-content">
                      Enter the number of classes that you want in your schedule. For instance enter "4" if you want to take four classes. This number must be less than the number of courses entered in the above field.
                    </span>
                  </span></p>
                    <div class="form__group">
                        <p><input name="combination_input" class="form__input" placeholder="4" required=""/></p>
                    </div>


                    <p class="ins">Must Include Sections
                    <span class="info-button">
                    <span class="info-icon"></span>
                    <span class="info-content">
                      Enter specific section numbers that you want included in your schedule. For example, type "CSC-161-01" if you only want schedules with the 1st section of CSC-161 included.
                    </span>
                  </span></p>
                    <div class="form__group">
                        <p><input name="include_input" class="form__input" placeholder="CSC-151-01 MAT-215-03"/></p>
                    </div>

                    <p class="ins">Must Exclude Sections
                    <span class="info-button">
                    <span class="info-icon"></span>
                    <span class="info-content">
                      Enter specific section numbers that you do not want included in your schedule. For example, type "CSC-161-01" if you want to take CSC-161, but not the 1st section.
                    </span>
                  </span></p>
                    <div class="form__group">
                        <p><input name="exclude_input" class="form__input" placeholder="PHI-111-01"/></p>
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
                    <p class="aboutus_p"><a id="githublink" target="_blank" href="https://github.com/closhu/unconflict">https://github.com/closhu/unconflict</a></p>
                    <p class="aboutus_st">contacts</p>
                    <p class="aboutus_p">kimgunwo@grinnell.edu<br>graysons@grinnell.edu<br>howellrh@grinnell.edu</p>
                    <p class="aboutus_st">about the project</p>
                    <br>
                    <div id="aboutproject">
                        <img src="/static/us.png" width="100%"><br><br>
                        We use recursive backtracking approach to generate every possible course combinations with no time conflicts.
                        Then, we display them according to user preference, including or excluding certain sections.
                    </div>
                    <br>

                </div>
            </div>
        </body>

        </html>
    '''


@app.route("/time", methods=["GET", "POST"])
def time_func():
    li = request.args.get('var1', '')
    li = li.split()
    for i, element in enumerate(li):
        if element[:2] == "L-":
            li[i-1] += "+"+element
            li.remove(element)

    html = f'''
        <html>
        <head>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div id="div-outermost">
                <div id="space_above"></div>
                <div id="div-flex">
                {timegraph(li)}
                </div>
            </div>
        </body>
        </html>
    '''

    return html
