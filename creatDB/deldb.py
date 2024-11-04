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

class delSampleInfo(db.Model):
    __tablename__ = 'delsampleinfo'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    projectBarcode = db.Column(db.String(20), index=True)
    projectName = db.Column(db.String(50), index=True)
    patientName = db.Column(db.String(10), index=True)
    patientID = db.Column(db.String(20), index=True)
    hospitalName = db.Column(db.String(50), index=True)
    sexName = db.Column(db.String(2))
    patientAge = db.Column(db.String(5))
    patientCardNo = db.Column(db.String(20))
    patientPhone = db.Column(db.String(20))
    sampleType = db.Column(db.String(20), index=True)
    hosDepartment = db.Column(db.String(20))
    patientNo = db.Column(db.String(20))
    bedNo = db.Column(db.String(20))
    doctorName = db.Column(db.String(20))
    clinicalDiagnosis = db.Column(db.String(100))
    sampleCollectionTime = db.Column(db.DateTime)
    sampleReceiveTime = db.Column(db.DateTime)
    diagnosisPeriod = db.Column(db.String(20), index=True)
    projectType = db.Column(db.String(20), index=True)
    reportTime = db.Column(db.DateTime)
    sampleStatus = db.Column(db.String(64), index=True)
    remark = db.Column(db.String(256))
    delOperator = db.Column(db.String(20), index=True)
    addtime = db.Column(db.DateTime, default=datetime.now)

class delextractANDpurify(db.Model):
    __tablename__ = 'delextractANDpurify'
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
    delOperator = db.Column(db.String(20), index=True)
    addtime = db.Column(db.DateTime, default=datetime.now)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
