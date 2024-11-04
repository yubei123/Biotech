from datetime import datetime, timedelta

def changeUTCtoLocal(utc_time):
    if 'T' in utc_time:
        a = datetime.strptime(utc_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        local_time = a + timedelta(hours=8)
    else:
        local_time = datetime.strptime(utc_time, "%Y-%m-%d %H:%M:%S")
    # Convert UTC time to local time
    # local_time = a + timedelta(hours=8)
    return local_time

def addOneday(utc_time):
    local_time = changeUTCtoLocal(utc_time) + timedelta(days=1)
    return local_time