from flask import Blueprint, request, jsonify, g
from app.models import User, SampleInfo
from app import db
from flask_jwt_extended import jwt_required
from datetime import datetime
from sqlalchemy import between, and_, or_
import os, requests

sample = Blueprint('sample', __name__)

# projects = {
#     'KBS001':{'projectName':'', 'projectType':''},
#     'KBS002':{'projectName':'', 'projectType':''},
#     'KBS003':{'projectName':'', 'projectType':''},
#     'KBS004':{'projectName':'', 'projectType':''}
# }

### 上传文件api
# @sample.route('/uploadfile', methods=['POST'])
# @jwt_required()
# def uploadfile():
#     today = datetime.now().strftime('%Y-%m-%d')
#     fileurl = request.files['file']
#     filename = fileurl.filename
#     if not os.path.isdir(f'/work/users/beitai/project/LymScan/sampleinfo/{today}'):
#         os.mkdir(f'/work/users/beitai/project/LymScan/sampleinfo/{today}')
#     savedir = f'/work/users/beitai/project/LymScan/sampleinfo/{today}/' + filename
#     fileurl.save(savedir)
#     res = {}
#     res['msg'] = 'upload success!'
#     res['code'] = 200
#     res['data'] = []
#     res['data'].append({'url': savedir})
#     print(res)
#     return jsonify(res)

### 样本信息更新api
@sample.route('/uploadsampleinfo', methods=['POST'])
@jwt_required()
def uploadsampleinfo():
    data = request.json['data']
    for i in data:
        info = SampleInfo.query.filter_by(sampleBarcode=i['sampleBarcode']).first()
        if info:
            info.update(**i)
        else:
            sample = SampleInfo(**i)
            db.session.add(sample)
    db.session.commit()

### lis系统获取样本信息api
@sample.route('/getsampleinfo', methods=['POST'])
@jwt_required()
def getsampleinfo():
    for i in request.json['data']:
        sampleBarcode = i['sampleBarcode']
        projectBarcode = i['projectBarcode']
        patientID = i['patientID']
        diagnosisPeriod = i['diagnosisPeriod']
        re = requests.post(f'https://tempest.kindstar.com.cn/aspid/login', json={"userName": "KSBT001","password": "1!2@3#4$fgh"}).json()
        token = re['tokenResponse']['access_token']
        headers = {}
        headers["Authorization"] = f"Bearer {token}"
        r = requests.get(f'https://itdevelop.kindstar.com.cn/api/external-common/api/SampleInfo/GetSampleByBacodeAndApplyItemCode?barcode={sampleBarcode}&applyitmeCode={projectBarcode}&affiliatedGroup=9030', headers=headers).json()
        if r['code'] == 'fail':
            return jsonify({'msg':'lis系统获取样本信息失败！', 'code': 204})
        sampledata = r['data']
        data = {
            'sampleBarcode':sampleBarcode,
            'projectBarcode':projectBarcode,
            'patientName':sampledata['patientName'],
            'patientID':patientID,
            'hospitalName':sampledata['hospitalName'] if sampledata['hospitalName'] else '-',
            'sexName':sampledata['sexName'] if sampledata['sexName'] else '-',
            'patientAge':sampledata['patientAgeDisplay'] if sampledata['patientAgeDisplay'] else '-',
            'patientCardNo':sampledata['patientCardNo'] if sampledata['patientCardNo'] else '-',
            'patientPhone':sampledata['patientPhone'] if sampledata['patientPhone'] else '-',
            'sampleType':sampledata['sampleTypeName'] if sampledata['sampleTypeName'] else '-',
            'hosDepartment':sampledata['hosDepartment'] if sampledata['hosDepartment'] else '-',
            'patientNo':sampledata['patientNo'] if sampledata['patientNo'] else '-',
            'bedNo':sampledata['bedNo'] if sampledata['bedNo'] else '-',
            'doctorName':sampledata['doctorName'] if sampledata['doctorName'] else '-',
            'clinicalDiagnosis':sampledata['clinicalDiagnosis'] if sampledata['clinicalDiagnosis'] else '-',
            'sampleCollectionTime':sampledata['sampleCollectionTime'] if sampledata['sampleCollectionTime'] else '-',
            'sampleReceiveTime':sampledata['CreateDate'] if sampledata['CreateDate'] else '-',
            'diagnosisPeriod':diagnosisPeriod,
            'projectType':sampledata['applyItemName'] if sampledata['applyItemName'] else '-',
            'reportTime':None,
            'sampleStatus':'已收样',
            }
        info = SampleInfo.query.filter_by(sampleBarcode=sampleBarcode).first()
        if not info:
            sampleinfo = SampleInfo(**data)
            db.session.add(sampleinfo)
            db.session.commit()
        else:
            data['patientID'] = info.patientID
            data['projectType'] = info.projectType
            data['reportTime'] = info.reportTime
            data['sampleStatus'] = info.sampleStatus
            info.update(**data)
            db.session.commit()
    return jsonify({'msg': 'success', 'code': 200})

### 样本信息查询api
@sample.route('/searchsampleinfo', methods=['POST'])
@jwt_required()
def searchsampleinfo():
    inputStr = request.json['input']
    info = SampleInfo.query.filter(or_(SampleInfo.sampleBarcode == inputStr, SampleInfo.patientName == inputStr, SampleInfo.projectBarcode == inputStr, \
                                       SampleInfo.sampleType == inputStr, SampleInfo.patientID == inputStr, SampleInfo.hospitalName.contains(inputStr))).all()
    if not info:
        return jsonify({'msg': 'no data', 'code': 204})
    else:
        res = []
        for i in info:
            res.append(i.to_dict())
        return jsonify({'msg': 'success', 'code': 200, 'data': res})

### 样本信息删除api
@sample.route('/deletesampleinfo', methods=['POST'])
@jwt_required()
def deletesampleinfo():
    sampleBarcode = request.json['sampleBarcode']
    info = SampleInfo.query.filter_by(sampleBarcode=sampleBarcode).first()
    db.session.delete(info)
    db.session.commit()
    return jsonify({'msg': 'success', 'code': 200})

### 样本信息下载api
@sample.route('/downloadsampleinfo', methods=['POST'])
@jwt_required()
def downloadsampleinfo():
    pass