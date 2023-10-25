#acknowledgement: giles, pythonanywhere
from flask import Flask, request

from processing import solution

app = Flask(__name__)
app.config["DEBUG"] = True

# just write like this here instead of style.css. lol
style = """
<style>
    #div-outermost {
        display: inline-block;
        background-color: rgb(220, 220, 220);
        width: 100vw;
        min-height: 100vh;
    }
    #div-flex {
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
    }
</style>
"""

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
                    {style}
                </head>
                <body>
                    <p>Your potential schedules are: {result}</p>
                    <p><a href="/">Click here to make a new schedule</a>
                </body>
            </html>
        '''.format(style=style, result=result)

    return '''
        <html>
            <head>
                {style}
            </head>
            <body>
            {errors}
                <div id="div-outermost">
                    <div id="div-flex">
                        <h1>Welcome to UnConflict:</h1>
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
    '''.format(style=style, errors=errors)
