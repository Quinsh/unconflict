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
        course_input = request.form["course_input"]
        combination_input = request.form["combination_input"]
        result = solution(course_input, combination_input)
        return '''
            <html>
                <body>
                    <p>Your potential schedules are: {result}</p>
                    <p><a href="/">Click here to make a new schedule</a>
                </body>
            </html>
        '''.format(result=result)

    return '''
        <html>
            <body>
            {errors}
                <p>Welcome to UnConflict:</p>
                <form method="post" action=".">
                    <p>Input Desired Classes</p>
                    <p><input name="course_input" /></p>
                    <p>Input Number of Classes in Schedule</p>
                    <p><input name="combination_input" /></p>
                    <p><input type="submit" value="Make Your Schedule!" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
