from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
# from openpyxl import load_workbook
from glob import glob

app = Flask(__name__)
app.config.from_pyfile('/work/users/beitai/backend/Biotech/config.py')
db = SQLAlchemy(app)

class experimenttohos(db.Model):
    __tablename__ = 'experimenttohos'
    id = db.Column(db.Integer, primary_key=True)
    labDate = db.Column(db.String(8), index=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    patientID = db.Column(db.String(20), index=True)
    diagnosisPeriod = db.Column(db.String(20), index=True)
    barcodeGroup = db.Column(db.String(10))
    labSite = db.Column(db.String(10))
    labUser = db.Column(db.String(20))
    inputNG = db.Column(db.Integer)
    qcDate = db.Column(db.String(8), index=True)
    pcrSite = db.Column(db.String(10), index=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

class qctohos(db.Model):
    __tablename__ = 'qctohos'
    id = db.Column(db.Integer, primary_key=True)
    qcDate = db.Column(db.String(8), index=True)
    igh = db.Column(db.Integer)
    igdh = db.Column(db.Integer)
    igk = db.Column(db.Integer)
    igl = db.Column(db.Integer)
    trbvj = db.Column(db.Integer)
    trbdj = db.Column(db.Integer)
    trg = db.Column(db.Integer)
    trd = db.Column(db.Integer)
    addtime = db.Column(db.DateTime, default=datetime.now)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()


