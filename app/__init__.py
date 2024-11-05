from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('../config.py')

jwt = JWTManager()
jwt.init_app(app)

db = SQLAlchemy()
db.app = app
db.init_app(app)

from app.user import user
from app.menu import menu
from app.sample import sample
from app.experiment import experiment
from app.expertohos import expertohos

app.register_blueprint(user, url_prefix="/api/user")
app.register_blueprint(menu, url_prefix="/api/menu")
app.register_blueprint(sample, url_prefix="/api/sample")
app.register_blueprint(experiment, url_prefix="/api/experiment")
app.register_blueprint(expertohos, url_prefix="/api/expertohos")