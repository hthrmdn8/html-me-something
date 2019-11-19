from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="POST">
            <label for="first-name">First Name:</label>
            <input id="first-name type="text" name="first_name"/>
            <label for="last-name">Last Name:</label>
            <input id="last-name type="text" name="last_name"/>
            <input type="submit"/>            
        </form>
    </body>
</html>        
"""

@app.route("/")
def index():
    return form
@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    return '<h1>Hello, ' + first_name + ' ' + last_name + " Yous a dumb Bitch</h1>"
app.run()