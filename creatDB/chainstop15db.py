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

class IGHtop15(db.Model):
    __tablename__ = 'IGHtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class IGDHtop15(db.Model):
    __tablename__ = 'IGDHtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class IGKtop15(db.Model):
    __tablename__ = 'IGKtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class KDEtop15(db.Model):
    __tablename__ = 'KDEtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)


class IGLtop15(db.Model):
    __tablename__ = 'IGLtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class TRBVJtop15(db.Model):
    __tablename__ = 'TRBVJtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class TRBDJtop15(db.Model):
    __tablename__ = 'TRBDJtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class TRDVJtop15(db.Model):
    __tablename__ = 'TRDVJtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class TRDDJtop15(db.Model):
    __tablename__ = 'TRDDJtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

class TRGtop15(db.Model):
    __tablename__ = 'TRGtop15'
    id = db.Column(db.Integer, primary_key=True)
    sampleBarcode = db.Column(db.String(50), index=True)
    labDate = db.Column(db.String(8), index=True)
    barcodeGroup = db.Column(db.String(10))
    top = db.Column(db.String(10))
    markerReads = db.Column(db.Integer)
    cloneFreq = db.Column(db.Float)
    cellRatio = db.Column(db.Float)
    ampFactor = db.Column(db.Float)
    markerCellsByN = db.Column(db.Float)
    markerSeq = db.Column(db.String(100))
    vGene = db.Column(db.String(100))
    jGene = db.Column(db.String(100))
    adjustedCellRatio = db.Column(db.Float)
    addtime = db.Column(db.DateTime, default=datetime.now)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()