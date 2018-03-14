#coding:utf-8
import time
import json
import urllib.request, urllib.error, urllib.parse
import random
import redis
import requests
requests.packages.urllib3.disable_warnings()
import MySQLdb
from warnings import filterwarnings
filterwarnings('ignore', category = MySQLdb.Warning)
test_db_ip = '192.168.1.101'
test_user = 'dddev'
test_passwd = '123456'
test_mainDb='ctcdb_new_test'
test_ckDb='ctcdb_ck_test'

ID=[99, 188, 77, 74, 22, 20, 76, 75, 98]
conn_test = MySQLdb.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306,charset="utf8")
cur=conn_test.cursor()
conn_test.select_db(test_mainDb)
info=cur.execute("select DISTINCT(MaintainerId) from stores WHERE MaintainerId !='NULL' and CityId=320400")
data=cur.fetchmany(info)
for i in data:
    ID.append(i[0])
cur.close()
conn_test.close()
print(ID)