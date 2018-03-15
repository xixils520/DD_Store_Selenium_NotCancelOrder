  #coding:utf-8
import pymysql
from warnings import filterwarnings
# filterwarnings('ignore', category = pymysql.Warning)
# test_db_ip = '192.168.1.101'
# test_user = 'dddev'
# test_passwd = '123456'
# test_mainDb='ctcdb_new_test'
# test_ckDb='ctcdb_ck_test'
# conn_test = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306,charset="utf8")
# nav_Name = raw_input(u'\n输入新建商品名标签(默认跳过):\n'.encode('gb18030'))
# print type(nav_Name)
# print nav_Name
# cur = conn_test.cursor()
# conn_test.select_db(test_mainDb)
# cur.execute("select id from goods where `name` = '%s'" % nav_Name.decode('gbk'))
# info = cur.fetchone()
# cur.close()
# print info
sss=[1,2,3,4,56,4]
ddd=[1,2,3,4,56,4]
ddd.pop()
print(ddd)
print(sss)
ddd=sss
print(ddd)
print(sss)
