import requests,sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from decimal import Decimal
from xlrd import open_workbook
from openpyxl import load_workbook
from top15models import IGHtop15,IGKtop15,IGLtop15,IGDHtop15,KDEtop15,TRBDJtop15,TRBVJtop15,TRDDJtop15,TRDVJtop15,TRGtop15

app = Flask(__name__)
app.config.from_pyfile('/work/users/beitai/backend/Biotech/config.py')
db = SQLAlchemy(app)

def updateData(input):
    with app.app_context():
        sampleBarcode = input.split('/')[-1].split('.')[0]
        wb = open_workbook(input)
        ws = wb.sheets()[0]
        for j in range(0, ws.nrows):
            l = [i.value for i in ws.row(j)]
            if l[0] == 'productivity':
                n = 1
                continue
            if n > 15:
                continue
            data = {
                    'sampleBarcode': sampleBarcode,
                    'top' : n,
                    'markerReads' : l[7],
                    'cloneFreq' : l[8],
                    'cellRatio' : l[9],
                    'ampFactor' : l[10],
                    'markerCellsByN' : l[11],
                    'markerSeq' : l[14],
                    'vGene' : l[15],
                    'jGene' : l[16],
                    'adjustedCellRatio' : 0,
                }
            if l[12] == 'IGH':
                ightop15 = IGHtop15(**data)
                db.session.add(ightop15)
            elif l[12] == 'IGH+':
                igdhtop15 = IGDHtop15(**data)
                db.session.add(igdhtop15)
            elif l[12] == 'IGK':
                igktop15 = IGKtop15(**data)
                db.session.add(igktop15)
            elif l[12] == 'IGK+':
                kdetop15 = KDEtop15(**data)
                db.session.add(kdetop15)
            elif l[12] == 'IGL':
                igdhtop15 = IGLtop15(**data)
                db.session.add(igdhtop15)
            elif l[12] == 'TRB':
                trbvjtop15 = TRBVJtop15(**data)
                db.session.add(trbvjtop15)
            elif l[12] == 'TRB+':
                trbdjtop15 = TRBDJtop15(**data)
                db.session.add(trbdjtop15)
            elif l[12] == 'TRD':
                trdvjtop15 = TRDVJtop15(**data)
                db.session.add(trdvjtop15)
            elif l[12] == 'TRD+':
                trddjtop15 = TRDDJtop15(**data)
                db.session.add(trddjtop15)
            elif l[12] == 'TRG':
                trgtop15 = TRGtop15(**data)
                db.session.add(trgtop15)
            n += 1
        db.session.commit()

if __name__ == "__main__":
    input = sys.argv[1]
    updateData(input)