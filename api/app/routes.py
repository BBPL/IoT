from flask import render_template
from app import app

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/home/<string:name>", methods=['POST', 'GET'])
def home(name):
    
    # check is
    return render_template("home.html", name=name)
