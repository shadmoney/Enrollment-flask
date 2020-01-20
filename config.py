import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x17\xb0\xba\xab\x8a\x860\xc4\x96\xccp\x9d\xab}<GV\x02\xe5\xb1?\xa8\x19\xdf\x98\\'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    