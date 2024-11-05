from flask import Blueprint, request, jsonify, g
from app.models import SampleInfo, experimenttohos, qctohos
from app import db
from app.utils import changeUTCtoLocal, addOneday
from flask_jwt_extended import jwt_required
from sqlalchemy import between

expertohos = Blueprint('expertohos', __name__)

### 导入实验信息
@expertohos.route('/inputexperinfo', methods=['POST'])
@jwt_required()
def inputexperinfo():
    data = request.json['data']
    # try:
    for i in data:
        exp = experimenttohos.query.filter(experimenttohos.sampleBarcode==i['sampleBarcode']).first()
        if exp:
            exp.update(**i)
        else:
            exp = experimenttohos(**i)
            db.session.add(exp)
    db.session.commit()
    return jsonify({'msg': 'success', 'code': 200})
    # except Exception as e:
    #     print(e)
    #     return jsonify({'msg': 'fail', 'code': 500})

@expertohos.route('/searchexperinfo', methods=['POST'])
@jwt_required()
def searchexperinfo():
    data = request.get_json()
    n = 0
    query = experimenttohos.query
    if data['sampleBarcode'] != '':
        query = query.filter(experimenttohos.sampleBarcode == data['sampleBarcode'])
        n += 1
    if data['patientID'] != '':
        query = query.filter(experimenttohos.patientID == data['patientID'])
        n += 1
    if data['labDate'] != '':
        query = query.filter(experimenttohos.labDate == data['labDate'])
        n += 1
    if data['diagnosisPeriod'] != '':
        query = query.filter(experimenttohos.diagnosisPeriod.contains(data['diagnosisPeriod']))
        n += 1
    if data['qcDate'] != '':
        query = query.filter(experimenttohos.qcDate == data['qcDate'])
        n += 1
    if data['pcrSite'] != '':
        query = query.filter(experimenttohos.pcrSite.contains(data['pcrSite']))
        n += 1
    if data['addtime'] != None:
        stime = changeUTCtoLocal(data["addtime"])
        etime = addOneday(data["addtime"])
        query = query.filter(between(experimenttohos.addtime, stime, etime))
        n += 1
    info = query.paginate(page=data['pagenum'], per_page=5)
    if not info or n == 0:
        return jsonify({'msg': 'no data', 'code': 204})
    else:
        res = []
        for i in info:
            res.append(i.to_json())
        return jsonify({'msg': 'success', 'code': 200, 'data': {'pages': info.pages, 'data':res}})

### 导入内参信息
@expertohos.route('/inputqcinfo', methods=['POST'])
@jwt_required()
def inputqcinfo():
    data = request.json['data']
    # try:
    for i in data:
        qcinfo = qctohos.query.filter(qctohos.qcDate==i['qcDate']).first()
        if qcinfo:
            qcinfo.update(**i)
        else:
            qcinfo = qctohos(**i)
            db.session.add(qcinfo)
    db.session.commit()
    return jsonify({'msg': 'success', 'code': 200})
    # except Exception as e:
    #     print(e)
    #     return jsonify({'msg': 'fail', 'code': 500})

@expertohos.route('/searchqcinfo', methods=['POST'])
@jwt_required()
def searchqcinfo():
    data = request.get_json()
    n = 0
    query = qctohos.query
    if data['qcDate'] != '':
        query = query.filter(qctohos.qcDate == data['qcDate'])
        n += 1
    info = query.paginate(page=data['pagenum'], per_page=5)
    if not info or n == 0:
        return jsonify({'msg': 'no data', 'code': 204})
    else:
        res = []
        for i in info:
            res.append(i.to_json())
        return jsonify({'msg': 'success', 'code': 200, 'data': {'pages': info.pages, 'data':res}})

