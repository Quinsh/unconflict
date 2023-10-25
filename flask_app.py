#acknowledgement: giles, pythonanywhere
from flask import Flask, request

from processing import solution

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
            temp.append(" ".join(comb_no_repeat[i]))
            temp.append('''</p>
                            <ul>''')
            for j, course in enumerate(comb_clusters[i]):
                temp.append("<li>")
                temp.append(" ".join(course))
                temp.append("</li>")
            temp.append('''</ul>
                        </div>''')
            formattedblocks.append(temp)
        
        return '''
            <html>
            <head>
                <link rel="stylesheet" href="./style.css">
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
            <head>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
            {errors}
                <div id="div-outermost">
                    <div id="space_above"></div>
                    <div id="div-flex">
                        <h1>UNCONFLICT</h1>
                        <p id="subtitle">course combinations at Grinnell</p>
                        <form method="post" action=".">
                            <p>Input Desired Classes</p>
                            <p><input name="course_input" /></p>
                            <p>Input Number of Classes in Schedule</p>
                            <p><input name="combination_input" /></p>
                            <p>Input Must Include Classes</p>
                            <p><input name="include_input" /></p>
                            <p>Input Must Exclude Classes</p>
                            <p><input name="exclude_input" /></p>
                            <p><input type="submit" value="Make Your Schedule!" /></p>
                        </form>
                    </div>
                </div>
            </body>
        </html>
    '''.format(errors=errors)
