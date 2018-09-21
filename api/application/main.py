from flask import Flask,Request,render_template
app = Flask(__name__, template_folder="../templates/")

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/home/<string:name>", methods=['POST', 'GET'])
def home(name):

    return render_template("home.html", name=name)