
from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from flask_jwt_extended import jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

user = Blueprint('user', __name__)

##获取token并登录
@user.post('/login')
def login():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'msg': f'用户不存在！', 'code': 401}
    if not check_password_hash(user.password, password):
        return {'msg': f'密码错误！', 'code': 401}
    return jsonify({'msg': '登录成功！','username':username, 'code': 200, 'token': user.generate_auth_token()})

##验证token是否有效
@user.get('/check_token')
@jwt_required()
def check_token():
    return jsonify({'msg':'success', 'code':200})

##注册新用户
@user.post('/addUser')
def addUser():
    username = request.json['username']
    password = request.json['password']
    department = request.json['department']
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'msg':'用户已存在！', 'code':401})
    else:
        u = User(username=username, password=generate_password_hash(password), department=department)
        db.session.add(u)
        db.session.commit()
        return jsonify({'msg':'注册成功！', 'code':200})

##修改用户密码
@user.post('/changePassword')
@jwt_required()
def changePassword():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if user:
        user.update(password=generate_password_hash(password))
        db.session.commit()
        return jsonify({'msg':'修改密码成功！', 'code':200})
    else:
        return jsonify({'msg':'用户不存在！', 'code':401})
