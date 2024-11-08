from flask import Blueprint, request, jsonify, g
from app.models import User, SampleInfo, delSampleInfo
from app import db
from flask_jwt_extended import jwt_required
from datetime import datetime
from sqlalchemy import between, and_, or_
import os, requests
from app.utils import changeUTCtoLocal, addOneday

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

### 样本信息上传及更新api
@sample.route('/uploadsampleinfo', methods=['POST'])
@jwt_required()
def uploadsampleinfo():
    data = request.json['data']
    tag = request.json['tag']
    # print(data)
    # try:
    dup = []
    if tag == 'edit':
        i = data[0]
        if i['sampleCollectionTime'] != None:
            i['sampleCollectionTime'] = changeUTCtoLocal(i['sampleCollectionTime'])
        if i['sampleReceiveTime'] != None:
            i['sampleReceiveTime'] = changeUTCtoLocal(i['sampleReceiveTime'])
        info = SampleInfo.query.filter_by(sampleBarcode=i['sampleBarcode']).first()
        if info:
            info.update(**i)
        else:
            sample = SampleInfo(**i)
            db.session.add(sample)
    else:
        for i in data:
            info = SampleInfo.query.filter_by(sampleBarcode=i['sampleBarcode']).first()
            if info:
                dup.append(i['sampleBarcode'])
        if dup != []:
            return jsonify({'msg':f'以下样本条码重复，请检查：{",".join(dup)}', 'code':222})
        
        for i in data:
            if i['sampleCollectionTime'] != None:
                i['sampleCollectionTime'] = changeUTCtoLocal(i['sampleCollectionTime'])
            if i['sampleReceiveTime'] != None:
                i['sampleReceiveTime'] = changeUTCtoLocal(i['sampleReceiveTime'])
            info = SampleInfo.query.filter_by(sampleBarcode=i['sampleBarcode']).first()
            if info:
                dup.append(i['sampleBarcode'])
            else:
                sample = SampleInfo(**i)
                db.session.add(sample)
    db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     return jsonify({'msg':'fail!', 'code':500})
    return jsonify({'msg':'success!', 'code':200})

### lis系统获取样本信息api
@sample.route('/getsampleinfo', methods=['POST'])
@jwt_required()
def getsampleinfo():
    dup_barcode = []
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
            data = i
        else:
            sampledata = r['data']
            data = {
                'sampleBarcode':sampleBarcode,
                'projectBarcode':projectBarcode,
                'projectName':sampledata['applyItemName'] if sampledata['applyItemName'] else '-',
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
                'sampleCollectionTime':sampledata['sampleCollectionTime'] if sampledata['sampleCollectionTime'] else None,
                'sampleReceiveTime':sampledata['createDate'] if sampledata['createDate'] else None,
                'diagnosisPeriod':diagnosisPeriod,
                'projectType':'临床项目',
                'reportTime':None,
                'sampleStatus':'已收样',
                }
        info = SampleInfo.query.filter_by(sampleBarcode=sampleBarcode).first()
        if not info:
            sampleinfo = SampleInfo(**data)
            db.session.add(sampleinfo)
        else:
            dup_barcode.append(info.sampleBarcode)
    db.session.commit()
    if dup_barcode != []:
        return jsonify({'msg': f'以下样本条码重复，请检查：{dup_barcode}', 'code': 222})
    return jsonify({'msg': 'success', 'code': 200})

### 样本信息查询api
@sample.route('/searchsampleinfo', methods=['POST'])
@jwt_required()
def searchsampleinfo():
    data = request.get_json()
    # print(data)
    n = 0
    query = SampleInfo.query
    if data['sampleBarcode'] != '':
        query = query.filter(SampleInfo.sampleBarcode == data['sampleBarcode'])
        n += 1
    if data['projectBarcode'] != '':
        query = query.filter(SampleInfo.projectBarcode == data['projectBarcode'])
        n += 1
    if data['projectName'] != '':
        query = query.filter(SampleInfo.projectName.contains(data['projectName']))
        n += 1
    if data['patientName'] != '':
        query = query.filter(SampleInfo.patientName.contains(data['patientName']))
        n += 1
    if data['patientID'] != '':
        query = query.filter(SampleInfo.patientID == data['patientID'])
        n += 1
    if data['hospitalName'] != '':
        query = query.filter(SampleInfo.hospitalName.contains(data['hospitalName']))
        n += 1
    if data['sampleType'] != '':
        query = query.filter(SampleInfo.sampleType.contains(data['sampleType']))
        n += 1
    if data['diagnosisPeriod'] != '':
        query = query.filter(SampleInfo.diagnosisPeriod.contains(data['diagnosisPeriod']))
        n += 1
    if data['projectType'] != '':
        query = query.filter(SampleInfo.projectType.contains(data['projectType']))
        n += 1
    if data['sampleStatus'] != '':
        query = query.filter(SampleInfo.sampleStatus.contains(data['sampleStatus']))
        n += 1
    if data['sampleCollectionTime'] != None:
        stime = changeUTCtoLocal(data["sampleCollectionTime"])
        etime = addOneday(data["sampleCollectionTime"])
        query = query.filter(between(SampleInfo.sampleCollectionTime, stime, etime))
        n += 1
    if data['addtime'] != None:
        stime = changeUTCtoLocal(data["addtime"])
        etime = addOneday(data["addtime"])
        query = query.filter(between(SampleInfo.addtime, stime, etime))
        n += 1
    info = query.paginate(page=data['pagenum'], per_page=5)
    a = [i.to_json() for i in info]
    if not a or n == 0:
        return jsonify({'msg': 'no data', 'code': 204})
    else:
        res = []
        for i in info:
            res.append(i.to_json())
        return jsonify({'msg': 'success', 'code': 200, 'data': {'pages': info.pages, 'data':res}})

### 样本信息删除api
@sample.route('/deletesampleinfo', methods=['POST'])
@jwt_required()
def deletesampleinfo():
    sampleBarcode = request.json['sampleBarcode']
    info = SampleInfo.query.filter_by(sampleBarcode=sampleBarcode).first()
    delinfo = info.to_json()
    delinfo['delOperator'] = g.username
    del delinfo['id']
    del delinfo['addtime']
    delsample = delSampleInfo(**delinfo)
    db.session.add(delsample)
    db.session.delete(info)
    db.session.commit()
    return jsonify({'msg': 'success', 'code': 200})