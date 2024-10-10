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

##创建用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(256))
    department = db.Column(db.String(64))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

##创建菜单表
class Menu(db.Model):
    __tablename__ = "menulist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    subname = db.Column(db.String(32), unique=True)
    subpath = db.Column(db.String(64), unique=True)
    department = db.Column(db.String(1024))

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
        test = User(username='test', password=generate_password_hash('123'), department='Laboratory')
        test2 = User(username='test2', password=generate_password_hash('123'), department='Bioinfo')
        test3 = User(username='test3', password=generate_password_hash('123'), department='Laboratory,Bioinfo')
        db.session.add(test)
        db.session.add(test2)
        db.session.add(test3)

        t = Menu(name='首页', subname='我的首页', subpath='/myhome', department='all')
        db.session.add(t)
        t = Menu(name='实验室处理', subname='样本录入', subpath='/SampleInput', department='Laboratory')
        db.session.add(t)
        t = Menu(name='实验室处理', subname='核酸提取', subpath='/NAExtraction', department='Laboratory')
        db.session.add(t)
        t = Menu(name='实验室处理', subname='文库构建', subpath='/LibraryConstruction', department='Laboratory')
        db.session.add(t)
        t = Menu(name='报告分析', subname='生信分析', subpath='/BioinfoAnalysis', department='Bioinfo')
        db.session.add(t)
        t = Menu(name='报告分析', subname='报告生成', subpath='/ReportGeneration', department='Bioinfo')
        db.session.add(t)
        t = Menu(name='报告分析', subname='报告审核', subpath='/ReportReview', department='Bioinfo')
        db.session.add(t)
        db.session.commit()
        # # t = Menu(name='系统管理', subname='功能设置', subpath='/SYSaddFunction', department='admin')
        # # db.session.add(t)
        # # t = Menu(name='系统管理', subname='日志查询', subpath='/SYSlogFunction', department='admin')
        # # db.session.add(t)
        

