from flask import Blueprint, request, jsonify, g
from app.models import SampleInfo, extractANDpurify
from app import db
from flask_jwt_extended import jwt_required
from datetime import datetime
from sqlalchemy import between, and_, or_
import os, requests

experiment = Blueprint('experiment', __name__)

### 点击开始实验，创建实验记录
@experiment.route('/createExtract', methods=['POST'])
@jwt_required()
def createExtract():
    data = request.json['data']
    tag = request.json['tag']
    allstatus = set([i['sampleStatus'] for i in data])
    if len(allstatus) != 1:
        return jsonify({'msg':'选择多个样本时检验状态需保持一致，请重新选择', 'code':400})
    dup = []
    try:
        for i in data:
            print(i)
            if i['sampleStatus'] == '已退项':
                continue
            newexp = {
                'sampleBarcode':i['sampleBarcode'],
                'projectBarcode':i['projectBarcode'],
                'projectName':i['projectName'],
                'projectType':i['projectType'],
                'patientName':i['patientName'],
                'patientID':i['patientID'],
                'diagnosisPeriod':i['diagnosisPeriod'],
                'sampleType':i['sampleType'],
                'sampleSentNum':'',
                'bloodVolume':'',
                'bloodUsed':'',
                'extractDNAVolume':'',
                'originalTubeConcentration':'',
                'extractTubes':'',
                'purifyQubitConcentration':'',
                'purifyDNAVolume':'',
                'purifyOperator':'',
                'purifyDate':None,
                'purifyStatus':'未开始',
                'remark':''
                }
            if tag == '补送':
                exp = extractANDpurify.query.filter(extractANDpurify.sampleBarcode==i['sampleBarcode']).all()
                if exp:
                    newexp['sampleSentNum'] = f'第 {len(exp) + 1} 次送样'
                    extract = extractANDpurify(**newexp)
                    db.session.add(extract)
                else:
                    return jsonify({'msg': f'{i["sampleBarcode"]}未进行过实验，请检查', 'code': 201})
            else:
                exp = extractANDpurify.query.filter(extractANDpurify.sampleBarcode==i['sampleBarcode']).all()
                if not exp:
                    newexp['sampleSentNum'] = '第 1 次送样'
                    extract = extractANDpurify(**newexp)
                    db.session.add(extract)
                else:
                    dup.append(i['sampleBarcode'])
                info = SampleInfo.query.filter(SampleInfo.sampleBarcode==i['sampleBarcode']).first()
                info.update(sampleStatus='提取纯化中')
        db.session.commit()
    except Exception as e:
        print(e)
    if dup != []:
        dups = ','.join(dup)
        return jsonify({'msg': f'以下样本已存在实验记录，请检查：{dups}', 'code': 222})
    return jsonify({'msg': 'success', 'code': 200})

### 更新提取纯化记录
@experiment.route('/updateExtract', methods=['POST'])
@jwt_required()
def updateExtract():
    data = request.json['data']
    try:
        for i in data:
            exp = extractANDpurify.query.filter(extractANDpurify.sampleBarcode==i['sampleBarcode']).first()
            exp.update(**i)
            info = SampleInfo.query.filter(SampleInfo.sampleBarcode==i['sampleBarcode']).first()
            if exp.purifyStatus == '合格':
                remark = exp.remark + f'{exp.sampleSentNum}:合格;'
                info.update(remark=remark)
            else:
                remark = exp.remark + f'{exp.sampleSentNum}:不合格;'
                info.update(remark=remark)
        db.session.commit()
    except Exception as e:
        print(e)
    return jsonify({'msg': 'success', 'code': 200})

### 搜索提取纯化记录
@experiment.route('/searchExtract', methods=['POST'])
@jwt_required()
def searchExtract():
    data = request.get_json()
    n = 0
    query = extractANDpurify.query
    if data['sampleBarcode'] != '':
        query = query.filter(extractANDpurify.sampleBarcode == data['sampleBarcode'])
        n += 1
    if data['projectBarcode'] != '':
        query = query.filter(extractANDpurify.projectBarcode == data['projectBarcode'])
        n += 1
    if data['projectName'] != '':
        query = query.filter(extractANDpurify.projectName.contains(data['projectName']))
        n += 1
    if data['patientName'] != '':
        query = query.filter(extractANDpurify.patientName.contains(data['patientName']))
        n += 1
    if data['purifyStatus'] != '':
        query = query.filter(extractANDpurify.purifyStatus == data['purifyStatus'])
        n += 1
    info = query.paginate(page=data['pagenum'], per_page=5)
    if not info or n == 0:
        return jsonify({'msg': 'no data', 'code': 204})
    else:
        res = []
        for i in info:
            res.append(i.to_json())
        return jsonify({'msg': 'success', 'code': 200, 'data': {'pages': info.pages, 'data':res}})