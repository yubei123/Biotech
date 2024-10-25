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

class extractANDpurify(db.Model):
    __tablename__ = 'extractANDpurify'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    projectBarcode = db.Column(db.String(20), index=True)
    projectName = db.Column(db.String(50), index=True)
    projectType = db.Column(db.String(20), index=True)
    patientName = db.Column(db.String(10), index=True)
    patientID = db.Column(db.String(20), index=True)
    diagnosisPeriod = db.Column(db.String(20), index=True)
    sampleType = db.Column(db.String(20), index=True)
    sampleSentNum = db.Column(db.String(20), index=True)
    bloodVolume = db.Column(db.String(20))
    bloodUsed = db.Column(db.String(20))
    extractDNAVolume = db.Column(db.String(20))
    originalTubeConcentration = db.Column(db.String(64))
    extractTubes = db.Column(db.String(10))
    purifyQubitConcentration = db.Column(db.String(20))
    purifyDNAVolume = db.Column(db.String(20))
    purifyOperator = db.Column(db.String(10))
    purifyDate = db.Column(db.DateTime)
    purifyStatus = db.Column(db.String(20), index=True)
    remark = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, default=datetime.now)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
