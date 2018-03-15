#coding:utf-8
import pymysql
from warnings import filterwarnings
filterwarnings('ignore', category = pymysql.Warning)
test_db_ip = '192.168.1.101'
test_user = 'dddev'
test_passwd = '123456'
test_mainDb='ctcdb_new_test'
test_ckDb='ctcdb_ck_test'
conn_test = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306,charset="utf8")
