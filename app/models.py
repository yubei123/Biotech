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
    
    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def generate_auth_token(self):
        pyload = {'username': self.username, 'department': self.department}
        token = create_access_token(identity=pyload, expires_delta=timedelta(seconds=600))
        return token

    def to_json(self):
        return serialize(self)

class Menu(db.Model):
    __tablename__ = "menulist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    subname = db.Column(db.String(32), unique=True)
    subpath = db.Column(db.String(64), unique=True)
    department = db.Column(db.String(1024))