from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('/work/users/beitai/backend/Biotech/config.py')
db = SQLAlchemy(app)

def serialize(self):
    json = {}
    for i in self.__table__.c:
        key = str(i.key)
        json[key] = getattr(self, key)
    return json

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)
    
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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)


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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)

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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_json(self):
        return serialize(self)