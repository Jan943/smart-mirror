from flask import Flask, render_template, request

app = Flask(__name__)

name = ""

@app.route('/')
def index():
    return render_template('index.html')

# implement endpoint for handling POST request from script for face
# recognition, save name from request

@app.route('/', methods = ["POST"])
def parse_request():
   request.get_data()
   global name
   name = request.data
   print(name)
   return ""
#    if request.method == "POST":
#        # Attempt the login & do something else
#    elif request.method == "GET":
#        return render_template("index.html")


# implement endpoint for handling get request from frontend and return saved earlier name


# def parse_request():
#   request.get_data()
#   global name
#   name = request.data
#   print(name)
#   return ""


if __name__ == '__main__':
    app.run(debug=True)
