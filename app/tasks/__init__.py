from celery import Celery
import subprocess
from flask import Flask
from app import db
from celery.schedules import crontab
from datetime import timedelta
from app.models import SampleInfo
from sqlalchemy import and_

apps = Flask(__name__)
apps.config.from_pyfile('/work/users/beitai/backend/Biotech/config.py')
db.init_app(apps)

broker = 'redis://127.0.0.1:6379/0'
backend = 'redis://127.0.0.1:6379/1'

celery_app = Celery('lym', broker=broker, backend=backend, include=["app.tasks"])

celery_app.conf.beat_schedule = {
    'runPipeline': {
        'task': 'app.tasks.runPipeline',
        'schedule': timedelta(seconds=20)
    },
}

@celery_app.task()
def onProcessPipline(sh):
    spp = subprocess.run(sh, shell=True, stderr=subprocess.PIPE)
    if spp.returncode == 0:
        return '运行脚本成功！'
    else:
        return f'运行脚本失败！{spp.stderr}'

### 监听数据库中未分析样本，确认原始数据是否存在并运行脚本
@celery_app.task
def runPipeline():
    with apps.app_context():
        unanalysis = SampleInfo.query.filter(and_(SampleInfo.sampleStatus != '已分析', SampleInfo.sampleStatus != '已退项')).all()
        for i in unanalysis:
            print(i.sampleBarcode)
