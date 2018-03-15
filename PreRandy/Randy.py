#coding:utf-8
import time
import json
import urllib.request, urllib.error, urllib.parse
import random
import redis
import requests
requests.packages.urllib3.disable_warnings()
import pymysql
from warnings import filterwarnings
filterwarnings('ignore', category = pymysql.Warning)
test_db_ip = '192.168.1.101'
test_user = 'dddev'
test_passwd = '123456'
test_mainDb='ctcdb_new_test'
test_ckDb='ctcdb_ck_test'
conn_test = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306,charset="utf8")

redis_db_ip='192.168.1.101'
redis_port=6379
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
store_url = 'http://192.168.1.251:30011'
global_url='http://192.168.1.251:39000'

def changeIntoStr(data,str_data=''):
    if isinstance(data, str):
        str_data = data.encode('utf-8')
    elif isinstance(data, str):
        str_data = data
    return str_data

def clean_redis(storePhoneNum):
    """
    清空缓存购物车信息
    """
    cur = conn_test.cursor()
    conn_test.select_db(test_mainDb)
    cur.execute("select id from stores where storePhoneNum = {0}".format(storePhoneNum))
    _ID=cur.fetchone()
    cur.close()
    rd = redis.Redis(host=redis_db_ip, port=redis_port, db=0)
    try:
        key_ = 'cart:{0}'.format(_ID[0])
        if rd.exists(key_):
            rd.delete(key_)
    except:
        pass

def checkStoreName(cityId,prehouse):
    """
    查询店铺
    """
    cur = conn_test.cursor()
    conn_test.select_db(test_mainDb)
    info=cur.execute("select id,storePhoneNum,storeName from stores where storeState= '1' and storePwd = 'e10adc3949ba59abbe56e057f20f883e' and CityId={0} order by id desc limit 60".format(cityId))
    storeInfo=cur.fetchmany(info)
    cur.close()

    cTime = 0
    dTime = 0
    if prehouse:
        prehouseId=[]
        cur1 = conn_test.cursor()
        if type(prehouse)==list:
            for pre in prehouse:
                conn_test.select_db(test_mainDb)
                info=cur1.execute("select StoreId from branch_warehouse_stores where CityId={0} and WarehouseId={1}".format(cityId,pre))
                preInfo=cur1.fetchmany(info)
                for pre in preInfo:
                    prehouseId.append(pre[0])
        else:
            conn_test.select_db(test_mainDb)
            info=cur1.execute("select StoreId from branch_warehouse_stores where CityId={0} and WarehouseId={1}".format(cityId,prehouse))
            preInfo=cur1.fetchmany(info)
            for pre in preInfo:
                prehouseId.append(pre[0])
        cur1.close()
        #判断
        prestore=[]
        mainstore=[]
        for store in storeInfo:
            if store[0] in prehouseId:
                prestore.append(store)
            else:
                mainstore.append(store)

        print('****************主仓店铺****************')
        for store in mainstore:
            print('店铺编号:',str(store[0]),'\t店铺登录账号:',str(store[1]),'\t店铺名:',store[2])
            cTime+=1
            if cTime>=4:
                break
        print('***************前置仓店铺***************')
        for store in prestore:
            print('店铺编号:',str(store[0]),'\t店铺登录账号:',str(store[1]),'\t店铺名:',store[2])
            dTime+=1
            if dTime>=4:
                break

    else:
        print('****************主仓店铺****************')
        for store in storeInfo:
            print('店铺编号:',str(store[0]),'\t店铺登录账号:',str(store[1]),'\t店铺名:',store[2])
            cTime+=1
            if cTime>=4:
                break
        print('**************无前置仓店铺***************')

def connectOnSellGoodsTable_onsell_CZ(cityid,Amount):
    new_good_id=[]
    cur =conn_test.cursor()
    conn_test.select_db('ctcdb_new_test')
    count_one = cur.execute("select id from on_sell_goods WHERE state= 100 and orderLimit=-1 and notSoldAreas='[]'  and  CityId='{0}' order by id desc limit {1}".format(cityid,Amount))
    info_one = cur.fetchmany(count_one)
    for info in info_one:
        new_good_id.append(info[0])
    cur.close()
    return new_good_id

def store_Order(purchase_phoneNum,good_id):
    # 登录
    session=requests.Session()
    login_url = '{0}/login'.format(store_url)
    session.post(url=login_url,data={'uid': purchase_phoneNum, 'pwd': '123456','auto': 'true',
                'plugin[sw]': 1920, 'plugin[sh]': 1080, 'plugin[iw]': 1916,
                'plugin[ih]': 264,'plugin[ua]': headers}, headers=headers)
    new_dict=dict()
    try:
        good_amount=random.randint(1,4)
        for i in range(int(good_amount)):
            add_good_url = '{0}/api/cart/up'.format(store_url)
            session.post(url=add_good_url,data={'command': json.dumps([{str(good_id): 'add'}])})
            session.post(url='http://192.168.1.251:30011/api/cart')
        new_dict[good_id] = good_amount
    except Exception as e:
        print('\n商品不存在')
    try:
        if new_dict:
            order_place_url='{0}/api/order/place'.format(store_url)
            order_place_response=session.post(url=order_place_url,data={'orders':json.dumps(new_dict),'dadou':0, 'redGiftId':'','couponCode':'-1','message':'','payType':'1'},headers=headers)
            order_place_str=changeIntoStr(order_place_response.text)
            order_place_json=json.loads(order_place_str)
            print('\n订单号为:',order_place_json['data']['id'])
            return order_place_json['data']['id']
    except Exception as e:
        print(e)
        print(order_place_json['message'])


def SureOrder(cityId,agencyId,service_url,service_username,service_password,orderID):
    #登陆客服
    time.sleep(2)
    newSession = requests.Session()
    service_login='{0}/service/api/manager/login'.format(service_url)
    service_response=newSession.post(url=service_login,data={'account':service_username,'password':service_password})
    #切换城市
    service_changecity_url='{0}/service/api/manager/updateAgency'.format(service_url)
    service_changecity_response=newSession.post(url=service_changecity_url,data={'cityId':cityId,'agencyId':agencyId})
    try:
        order_url='{0}/service/api/order/send'.format(service_url)
        order_res=newSession.post(url=order_url,data={'orderId':int(orderID)})
        order_json=json.loads(changeIntoStr(order_res.text))
        if order_json['tag']=='success':
            print('\n订单号:%s\t 审核通过\n'%orderID)
            return orderID
    except Exception as e:
        pass
def CancleOrder(cityId,agencyId,service_url,service_username,service_password,orderId):
    #登陆客服
    newSession = requests.Session()
    service_login='{0}/service/api/manager/login'.format(service_url)
    newSession.post(url=service_login,data={'account':service_username,'password':service_password})
    #切换城市
    service_changecity_url='{0}/service/api/manager/updateAgency'.format(service_url)
    newSession.post(url=service_changecity_url,data={'cityId':cityId,'agencyId':agencyId})
    #取消订单
    cancle_url='{0}/service/api/order/cancel'.format(service_url)
    cancle_response=newSession.post(url=cancle_url,data={'id':orderId,'info':'客户下错单'})
    cancle_json=json.loads(changeIntoStr(cancle_response.text))
    if cancle_json['tag']=='error':
        print('未找到对应货品订单')
    else:
        print('\n订单号:%s\t 取消订单成功\n' % str(orderId))

def mainstorerun(cityId, agencyId, server_url, url_username, url_password, orderId):
    time.sleep(3)
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
    login_url = '{0}/users/login'.format(server_url)
    login_data = {'userName': url_username, 'password': url_password}
    session.post(url=login_url, data=login_data, headers=headers)
    # 切换城市
    zdh_url = '{0}/users/updateAgency'.format(server_url)
    zdh_data = {'cityId': cityId, 'agencyId': agencyId}
    session.post(url=zdh_url, data=zdh_data, headers=headers)
    # 增加供应商
    numID = 0
    for i in range(6):
        boci_url = '{0}/api/expressRoute/create/surplus'.format(server_url)
        session.post(url=boci_url,
                     data={"orderTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 5 * 60))})
        conn_test1 = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
        cur = conn_test1.cursor()
        conn_test1.select_db(test_ckDb)
        cur.execute("select ExpressRouteId  from express_route_details where StoreGoodsOrderId='{0}'".format(orderId))
        data = cur.fetchone()
        cur.close()
        conn_test1.close()
        if data:
            numID = data[0]
            break
        else:
            time.sleep(2)
    if numID:
        sureoder_url = '{0}/api/pickGoods/pickList/create?id={1}'.format(server_url, numID)
        JH = session.get(url=sureoder_url, headers=headers)
        print(JH.text)
        time.sleep(20)
        conn_test2 = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
        cur = conn_test2.cursor()
        conn_test2.select_db(test_ckDb)
        info = cur.execute(
            "select a.PickListId, a.id,a.orderQuantity,a.actualQuantity,b.numberId  from pick_list_details as a,pick_lists as b where a.PickListId=b.id and b.ExpressRouteId={0}".format(
                numID))
        data_all = cur.fetchmany(info)
        cur.close()
        conn_test2.close()
        if data_all:
            token_url = '{0}/api/getToken?numberId={1}&key=JHQR'.format(server_url, data_all[0][4])
            token_data = session.get(url=token_url, headers=headers)
            token_json = json.loads(token_data.text)
            token = token_json['token']

            jianhuo_url = '{0}/api/pickGoods/pickList/confirm'.format(server_url)
            dict_can = {}
            for j in range(len(data_all)):
                dict_can['details[%d][pickListId]' % j] = data_all[j][0]
                dict_can['details[%d][detailId]' % j] = data_all[j][1]
                dict_can['details[%d][orderQuantity]' % j] = data_all[j][2]
                dict_can['details[%d][actualQuantity]' % j] = data_all[j][2]

            dict_can['pickGoodsName'] = 'pickman'
            dict_can['token'] = token
            session.post(url=jianhuo_url, data=dict_can, headers=headers)
            if str(cityId) == str(320100):
                print('配送员:', 'ps001', '\t配送员手机号:  15575000999\n')
                ps = 'ps001'
                courierId = 42
                name='11'
            elif str(cityId) == str(320200):
                print('配送员:', 'ps001', '\t配送员手机号:  15575000995\n')
                ps = 'ps001'
                courierId = 34
                name='00'
            else:
                print('配送员:', 'ps001', '\t配送员手机号:  17621145336\n')
                courierId = 14
                ps = 'ps001'
                name='李白'

            reviewOrder_url='http://192.168.1.251:48000/api/stockOut/scan/reviewOrder?orderId={0}&courierId={1}&virtualCourierId={2}&courierName={3}'.format(orderId,courierId,ps,urllib.parse.quote(name.encode('utf-8')))
            session.get(url=reviewOrder_url)
            confirm_Url='http://192.168.1.251:48000/api/stockOut/delivery/reviewConfirm'
            confirm_res=session.post(url=confirm_Url,data={'orderId':orderId,'courierId':courierId})
            confirm_json=json.loads(changeIntoStr(confirm_res.text))
            if confirm_json['tag']=='success':
                print('\n出库成功')
        else:
            pass

def prestorerun(cityId,agencyId,server_url,url_username,url_password,orderId):
    time.sleep(3)
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
    login_url = '{0}/users/login'.format(server_url)
    login_data = {'userName': url_username, 'password': url_password}
    session.post(url=login_url, data=login_data, headers=headers)
    # 切换城市
    zdh_url = '{0}/users/updateAgency'.format(server_url)
    zdh_data = {'cityId': cityId, 'agencyId': agencyId}
    session.post(url=zdh_url, data=zdh_data, headers=headers)
    # 增加供应商
    numID=0
    for i in range(6):
        boci_url = '{0}/api/expressRoute/create/surplus'.format(server_url)
        session.post(url=boci_url, data={"orderTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 5 * 60))})
        conn_test1 = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
        cur = conn_test1.cursor()
        conn_test1.select_db(test_ckDb)
        cur.execute("select ExpressRouteId  from express_route_details where StoreGoodsOrderId='{0}'".format(orderId))
        data = cur.fetchone()
        cur.close()
        conn_test1.close()
        if data:
            numID=data[0]
            break
        else:
            time.sleep(2)
    if numID:
        sureoder_url = '{0}/api/pickGoods/pickList/create?id={1}'.format(server_url, numID)
        JH=session.get(url=sureoder_url,headers=headers)
        print(JH.text)
        time.sleep(2)
        conn_test2 = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
        cur = conn_test2.cursor()
        conn_test2.select_db(test_ckDb)
        info=cur.execute("select a.PickListId, a.id,a.orderQuantity,a.actualQuantity,b.numberId  from pick_list_details as a,pick_lists as b where a.PickListId=b.id and b.ExpressRouteId={0}".format(numID))
        data_all=cur.fetchmany(info)
        cur.close()
        conn_test2.close()
        if data_all:
            token_url='{0}/api/getToken?numberId={1}&key=JHQR'.format(server_url,data_all[0][4])
            token_data=session.get(url=token_url,headers=headers)
            token_json=json.loads(token_data.text)
            token=token_json['token']

            jianhuo_url='{0}/api/pickGoods/pickList/confirm'.format(server_url)
            dict_can={}
            for j in range(len(data_all)):
                dict_can['details[%d][pickListId]'%j]=data_all[j][0]
                dict_can['details[%d][detailId]'%j]=data_all[j][1]
                dict_can['details[%d][orderQuantity]'%j]=data_all[j][2]
                dict_can['details[%d][actualQuantity]'%j]=data_all[j][2]

            dict_can['pickGoodsName']='pickman'
            dict_can['token']=token
            session.post(url=jianhuo_url,data=dict_can,headers=headers)

            if str(cityId)==str(320100):
                print('司机:','7777','\t司机手机号:  13900000000\n')
                ps='7777'
                courierId =8
                name='梅梅'
            elif str(cityId)==str(320200):
                print('司机:','sj001 ','\t司机手机号:  15000779522\n')
                ps = 'sj001'
                courierId =36
                name='ssss'
            else:
                print('司机:','sj002','\t司机手机号:  13200001111\n')
                courierId = 47
                ps = 'sj002'
                name='郭靖'
            reviewOrder_url='http://192.168.1.251:48000/api/stockOut/scan/reviewOrder?orderId={0}&courierId={1}&virtualCourierId={2}&courierName={3}'.format(orderId,courierId,ps,urllib.parse.quote(name.encode('utf-8')))
            session.get(url=reviewOrder_url)
            confirm_Url='http://192.168.1.251:48000/api/stockOut/delivery/reviewConfirm'
            confirm_res=session.post(url=confirm_Url,data={'orderId':orderId,'courierId':courierId})
            json.loads(changeIntoStr(confirm_res.text))
            sj_url='{0}/api/truckLoadList/courier/unload/list'.format(server_url)
            sj_response=session.post(url=sj_url,data={'CourierId':courierId})
            sj_json=json.loads(changeIntoStr(sj_response.text))

            ZC_id=0
            for sj_n in sj_json['data']:
                if sj_n['numberId'].split('-')[-1]==str(orderId):
                    ZC_id=sj_n['id']
            if ZC_id:
                ZC_url='{0}/api/truckLoadList/create'.format(server_url)
                session.post(url=ZC_url,data={'courierId':courierId,'orders[]':ZC_id})
                print(str(orderId), '\t前置仓订单波次已装车')

def main():
    cityChange = {'nanJin': {'cityId': 320100, 'agencyId': 101,'mainhouse':13,'prehouse':22}, 'changZhou': {'cityId': 320400, 'agencyId': 3,'mainhouse':1,'prehouse':False},
                  'wuXi': {'cityId': 320200, 'agencyId': 17,'mainhouse':4,'prehouse':[15,16,17]}, 'lianYunGang': {'cityId': 320700, 'agencyId': 171,'mainhouse':80,'prehouse':81}}
    print()
    while True:
        print('*'*30)
        print('请选择以下业务(输入数字选择):')
        order_num=input('\n\n1.商城下单->客服系统审核通过->仓库运输系统走单,\n\n0.退出,\n')
        if str(order_num)==str(1):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                prehouse = cityChange['nanJin']['prehouse']
                agencyId=cityChange['nanJin']['agencyId']
                server_url = 'http://192.168.1.251:3586'
                invent_url = 'http://192.168.1.251:48000'
                url_username = '12345678910'
                invent_username='12345678910'
                url_password = '123456'
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                prehouse = cityChange['wuXi']['prehouse']
                agencyId=cityChange['wuXi']['agencyId']
                server_url = 'http://192.168.1.251:3586'
                invent_url = 'http://192.168.1.251:48000'
                url_username = '12345678910'
                invent_username = '13111111111'
                url_password = '123456'
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                prehouse = cityChange['lianYunGang']['prehouse']
                agencyId=cityChange['lianYunGang']['agencyId']
                server_url = 'http://192.168.1.251:3586'
                invent_url = 'http://192.168.1.251:48000'
                url_username = '12345678910'
                invent_username = '12345678910'
                url_password = '123456'
            else:
                continue
            checkStoreName(cityId, prehouse)
            purchase_phoneNum = input('\n输入商城店铺登陆账号:\n')
            store_type = input('\n1.主仓店铺,\t2.前置仓店铺\n')
            amount=input('\n输入测试次数:\n')
            # list_SJ=connectOnSellGoodsTable_onsell_CZ(cityId,amount)
            #126043,126047,126042,
            list_SJ=[126043,126045,126047,126042,126044 ,126046,126048,126049,126051]
            for i in range(100):
                clean_redis(purchase_phoneNum)
                good_sj=random.sample(list_SJ,1)[0]
                print('上架编号:',str(good_sj))
                orderID =store_Order(purchase_phoneNum,good_sj)
                if orderID:
                    orderID=SureOrder(cityId, agencyId, server_url, url_username, url_password,orderID)
                    if orderID and store_type==str(1):
                        mainstorerun(cityId, agencyId, invent_url, invent_username, url_password,orderID)
                        time.sleep(10)
                    elif orderID and store_type==str(2):
                        prestorerun(cityId, agencyId, server_url, url_username, url_password, orderID)
                        time.sleep(10)
                    else:
                        print('异常不执行')
        elif str(order_num)==str(0):
            break
        else:
            continue
main()
