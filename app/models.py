from app import db, jwt
from datetime import timedelta, datetime
from flask_jwt_extended import create_access_token
from functools import wraps
from flask import g

@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return {'msg': 'Token已过期！', 'code': 401}

@jwt.token_verification_loader
def my_token_verification_callback(jwt_header, jwt_payload):
    g.username = jwt_payload['sub']['username']
    g.department = jwt_payload['sub']['department']
    return True

def serialize(self):
    json = {}
    for i in self.__table__.c:
        key = str(i.key)
        json[key] = getattr(self, key)
    return json

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(256))
    department = db.Column(db.String(64))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    
    def generate_auth_token(self):
        pyload = {'username': self.username, 'department': self.department}
        token = create_access_token(identity=pyload, expires_delta=timedelta(seconds=7200))
        return token
    
    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

class Menu(db.Model):
    __tablename__ = "menulist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    subname = db.Column(db.String(32), unique=True)
    subpath = db.Column(db.String(64), unique=True)
    department = db.Column(db.String(1024))

class SampleInfo(db.Model):
    __tablename__ = 'sampleinfo'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), unique=True, index=True)
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
    addtime = db.Column(db.DateTime, default=datetime.now)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def to_json(self):
        return serialize(self)
    
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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def to_json(self):
        return serialize(self)