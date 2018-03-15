#coding:utf-8
import pymysql
import json
import urllib.request, urllib.error, urllib.parse
import time
import requests
from warnings import filterwarnings
filterwarnings('ignore', category = pymysql.Warning)
test_db_ip = '192.168.1.101'
test_user = 'dddev'
test_passwd = '123456'
test_mainDb='ctcdb_new_test'
test_ckDb='ctcdb_ck_test'
conn_test = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306,charset="utf8")

def changeIntoStr(data,str_data=''):
    if isinstance(data, str):
        str_data = data.encode('utf-8')
    elif isinstance(data, str):
        str_data = data
    return str_data

def ZP_order(cityId,agencyId,invent_url,url_username,url_password,warehouseId,orderId,wid):
    # 登录
    NewSession=requests.Session()
    login_url = '{0}/users/login'.format(invent_url)
    login_data = {'userName': url_username, 'password': url_password}
    NewSession.post(url=login_url, data=login_data)
    zdh_url = '{0}/users/updateAgency'.format(invent_url)
    zdh_data = {'cityId':cityId,'agencyId':agencyId}
    NewSession.post(url=zdh_url, data=zdh_data)
    conn_test_A = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
    cur_A = conn_test_A.cursor()
    conn_test_A.select_db(test_ckDb)
    cur_A.execute("select id,rgl_number_id,rgl_store_goods_order_id,createdAt FROM return_goods_list where rgl_state='0' and rgl_warehouse_id='{0}'and rgl_store_goods_order_id='{1}' order by id desc".format(warehouseId,orderId))
    zp = cur_A.fetchone()
    cur_A.close()
    conn_test_A.close()
    if zp:
        print('\n退货单号:',str(zp[1]),'\t订单编号:',str(zp[2]),'\t创建时间',zp[3])
        TH_url='{0}/api/returnGoods/updateCourier'.format(invent_url)
        TH_res=NewSession.post(url=TH_url,data={'id':zp[0],'courierId':wid})
        TH_json=json.loads(changeIntoStr(TH_res.text))
        if TH_json['tag']=='success':
            print('\n指派配送员OK')

def TH_RU(cityId,agencyId,invent_url,url_username,url_password,warehouseId,orderId):
    # 登录
    NewSession=requests.Session()
    login_url = '{0}/users/login'.format(invent_url)
    login_data = {'userName': url_username, 'password': url_password}
    NewSession.post(url=login_url, data=login_data)
    zdh_url = '{0}/users/updateAgency'.format(invent_url)
    zdh_data = {'cityId':cityId,'agencyId':agencyId}
    NewSession.post(url=zdh_url, data=zdh_data)
    conn_test_A = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
    cur_A = conn_test_A.cursor()
    conn_test_A.select_db(test_ckDb)
    cur_A.execute("select id,rgl_number_id,rgl_store_goods_order_id,createdAt FROM return_goods_list where rgl_state='20' and rgl_warehouse_id='{0}'and rgl_store_goods_order_id='{1}' order by id desc".format(warehouseId,orderId))
    zp = cur_A.fetchone()
    cur_A.close()
    if zp:
        print('\n退货单号:',str(zp[1]),'\t订单编号:',str(zp[2]),'\t创建时间',zp[3])
        cur_B = conn_test_A.cursor()
        conn_test_A.select_db(test_ckDb)
        cur_B.execute("select id FROM return_goods_list_details where  rgld_return_goods_list_id='{0}' order by id desc".format(zp[0]))
        zp_B = cur_B.fetchone()
        cur_B.close()
        conn_test_A.close()
        if zp_B:
            return_url='{0}/api/returnGoods/list'.format(invent_url)
            NewSession.post(url=return_url,data={'numberId':str(zp[1])})
            confirm_url='{0}/api/returnGoods/confirm'.format(invent_url)
            confirm_res=NewSession.post(url=confirm_url,data={'id':zp[0],'details[0][id]':zp_B[0],'details[0][produceDate]':time.strftime('%Y-%m-%d',time.localtime(time.time()))})
            confirm_json=json.loads(changeIntoStr(confirm_res.text))
            if confirm_json['tag']=='success':
                print('\n已入库')

def SJ(cityId,agencyId,invent_url,url_username,url_password,warehouseId,orderId):
    # 登录
    if str(cityId)==str(320100):
        area ={'JH':'A01-01-01-01'}
    elif str(cityId)==str(320200):
        area ={'JH':'A01-01-01-01'}
    else:
        area={'JH': 'AA11-11-11-11'}
    print('\n默认上架拣货位:',area['JH'])
    SJ_area = input('\n输入要上架的位置(按Enter跳过即使用拣货位):'.encode('gb18030'))
    if SJ_area!='':
        area['JH']=SJ_area
    NewSession=requests.Session()
    login_url = '{0}/users/login'.format(invent_url)
    login_data = {'userName': url_username, 'password': url_password}
    NewSession.post(url=login_url, data=login_data)
    zdh_url = '{0}/users/updateAgency'.format(invent_url)
    zdh_data = {'cityId':cityId,'agencyId':agencyId}
    NewSession.post(url=zdh_url, data=zdh_data)
    conn_test_A = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
    cur_A = conn_test_A.cursor()
    conn_test_A.select_db(test_ckDb)
    cur_A.execute("select identificationCode  FROM check_up_orders where state='999' and WarehouseId='{0}'and StockInOrderId='{1}' order by id desc limit 1".format(warehouseId,orderId))
    zp = cur_A.fetchone()
    cur_A.close()
    conn_test_A.close()
    if zp:
        getToken_url='%s/api/getToken?numberId=%s&key=SJ'%(invent_url,zp[0])
        getToken_res=NewSession.get(url=getToken_url)
        getToken_json=json.loads(getToken_res.text)
        token=getToken_json['token']
        onRack_url='{0}/api/onRack/createOnRack'.format(invent_url)
        NewSession.post(url=onRack_url,data={'identificationCode':zp[0],'token':token})

        conn_test_B = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
        cur_B = conn_test_B.cursor()
        conn_test_B.select_db(test_ckDb)
        cur_B.execute("select id,numberId FROM on_racks where state='0' and WarehouseId='{0}'and checkUpOrderId='{1}' order by id desc limit 1".format(warehouseId, zp[0]))
        zp_B = cur_B.fetchone()
        cur_B.execute("select id FROM on_rack_details where OnRackId='{0}' order by id desc limit 1".format(zp_B[0]))
        zp_BB=cur_B.fetchone()
        cur_B.close()
        conn_test_B.close()
        viewOnRack_url='{0}/api/onRack/viewOnRackDetail'.format(invent_url)
        viewOnRack_res=NewSession.post(url=viewOnRack_url,data={'onRackId':zp_B[0],'id':zp_BB[0]})
        viewOnRack_json=json.loads(changeIntoStr(viewOnRack_res.text))
        getOToken_url='%s/api/getToken?numberId=%s&key=SJ'%(invent_url,zp_B[1])
        getOToken_res=NewSession.get(url=getOToken_url)
        getOToken_json=json.loads(changeIntoStr(getOToken_res.text))
        OToken=getOToken_json['token']
        verification_url='{0}/api/onRack/verification'.format(invent_url)
        verification_res=NewSession.post(url=verification_url,data={'param[0][onRackDetailId]':viewOnRack_json['data'][0]['id'],
                                                                    'param[0][GoodId]':viewOnRack_json['data'][0]['GoodId'],
                                                                    'param[0][quantity]':viewOnRack_json['data'][0]['quantity'],
                                                                    'param[0][produceDate]':viewOnRack_json['data'][0]['produceDate'],
                                                                    'param[0][targetPosition]':area['JH'],
                                                                    'param[0][LPN]':'','param[0][onRackId]':zp_B[0],
                                                                    'param[0][index]':0})
        verification_json=json.loads(changeIntoStr(verification_res.text))
        if verification_json['tag']=='success':
            onRackUpdate_url='{0}/api/onRack/update'.format(invent_url)
            onRackUpdate_res=NewSession.post(url=onRackUpdate_url,data={'param[0][onRackDetailId]':viewOnRack_json['data'][0]['id'],
                                                                        'param[0][GoodId]':viewOnRack_json['data'][0]['GoodId'],
                                                                        'param[0][quantity]':viewOnRack_json['data'][0]['quantity'],
                                                                        'param[0][produceDate]':viewOnRack_json['data'][0]['produceDate'],
                                                                        'param[0][targetPosition]':area['JH'],
                                                                        'param[0][LPN]':'','param[0][onRackId]':zp_B[0],
                                                                        'param[0][index]':0,
                                                                        'param[0][id]':verification_json['param'][0]['id'],
                                                                        'param[0][type]':verification_json['param'][0]['type'],
                                                                        'onRackOperator':'倔强的小强',
                                                                        'token':OToken})
            onRackUpdate_json=json.loads(changeIntoStr(onRackUpdate_res.text))
            if onRackUpdate_json['tag']=='success':
                print('\n上架成功')
        else:
            print('\n系统无相应库位号')

def TTT():
    conn_test_N = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
    cur_N = conn_test_N.cursor()
    conn_test_N.select_db(test_mainDb)
    cur_N.execute("select * from stock_in_orders WHERE state='0' and ProviderId='{0}' and sumWithTax='{1}'order by id desc limit 1 ".format(100716,24))
    info = cur_N.fetchone()
    print(info)
    if info:
        orderId = info[0]
        print('\n采购单号为', str(orderId))
    cur_N.close()
    conn_test_N.close()


def mainstorerun(cityId, agencyId, server_url, url_username, url_password, orderId):
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
    for i in range(5):
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
        conn_test2 = pymysql.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306, charset="utf8")
        cur = conn_test2.cursor()
        conn_test2.select_db(test_ckDb)
        info = cur.execute(
            "select a.PickListId, a.id,a.orderQuantity,a.actualQuantity,b.numberId  from pick_list_details as a,pick_lists as b where a.PickListId=b.id and b.ExpressRouteId={0}".format(
                numID))
        data_all = cur.fetchmany(info)
        cur.close()
        conn_test2.close()
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

# worker = {'name':u'李白','id':14,'workId':'ps001','phone':17621145336}
# ZP_order(320700,171,'http://192.168.1.251:48000',12345678910,123456,80,11116778,14)
# TH_RU(320700,171,'http://192.168.1.251:48000',12345678910,123456,80,11117060)

mainstorerun(320700, 171,'http://192.168.1.251:48000' ,12345678910,123456,'11117162')