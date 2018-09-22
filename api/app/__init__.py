from flask import Flask,Request,render_template
from models import satellite
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__, template_folder="../templates/")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')