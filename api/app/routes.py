from flask import render_template
from app import app,db
from app.models import Satellite

@app.route("/")
def hello():
    return ("Hello world")


@app.route("/home/<string:name>", methods=['POST', 'GET'])
def home(name):
    s = Satellite.query.filter(Satellite.name == name)
    if not s.first():
        return render_template("home.html", name="fuck")
    return render_template("home.html", name=s.first().name)


@app.route("/connect/<string:ip>/<int:port>/<string:name>")
def connectSatellite(ip,port,name):
    s = Satellite.query.filter(Satellite.ip == ip).filter(Satellite.port == port)
    if not s.first(): #if no results found
        satellite = Satellite(ip=ip,port=port,name=name)
        db.session.add(satellite)
        db.session.commit()
        return("added!")
    return("nope!")
        
