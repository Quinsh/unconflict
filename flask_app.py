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
        result = solution(course_input, combination_input, include_input, exclude_input)
        return '''
            <html>
                <head>
                    <link rel="stylesheet" href="./style.css">
                </head>
                <body>
                    <p>Your potential schedules are: {result}</p>
                    <p><a href="/">Click here to make a new schedule</a>
                </body>
            </html>
        '''.format(result=result)

    return '''
        <html>
            <head>
                <link rel="stylesheet" href="./style.css">
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
