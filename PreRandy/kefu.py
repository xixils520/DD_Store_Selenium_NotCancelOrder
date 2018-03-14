#coding:utf-8
import MySQLdb
import json
import time
import requests
from warnings import filterwarnings
filterwarnings('ignore', category = MySQLdb.Warning)
test_db_ip = '192.168.1.101'
test_user = 'dddev'
test_passwd = '123456'
test_mainDb='ctcdb_new_test'
test_ckDb='ctcdb_ck_test'
conn_test = MySQLdb.connect(host=test_db_ip, user=test_user, passwd=test_passwd, port=3306,charset="utf8")

def changeIntoStr(data,str_data=''):
    if isinstance(data, str):
        str_data = data.encode('utf-8')
    elif isinstance(data, str):
        str_data = data
    return str_data

def CancleOrder(cityId,agencyId,service_url,service_username,service_password,orderId):
    #登陆客服
    newSession = requests.Session()
    service_login='{0}/service/api/manager/login'.format(service_url)
    newSession.post(url=service_login,data={'account':service_username,'password':service_password})
    #切换城市
    service_changecity_url='{0}/service/api/manager/updateAgency'.format(service_url)
    newSession.post(url=service_changecity_url,data={'cityId':cityId,'agencyId':agencyId})
    #点单明细
    cur = conn_test.cursor()
    conn_test.select_db(test_mainDb)
    cur.execute("select id FROM store_order_branches where StoreGoodsOrderId='{0}' and CityId='{1}'".format(orderId,cityId))
    data = cur.fetchone()
    print(data[0])
    cur.close()
    detail_url='{0}/service/api/backGoods/branchOrder/detail'.format(service_url)
    detail_res=newSession.post(url=detail_url,data={'orderId':orderId,'branchOrderId':data[0]})
    detail_json=json.loads(changeIntoStr(detail_res.text))
    new_detail=[]
    for de in detail_json['result']:
        new_detail.append(de)
    back_url = '{0}/service/api/backGoods/add'.format(service_url)
    if len(new_detail)==1:
        print('\n商品可退总数为:',str(int(new_detail[0]['amount'])-int(new_detail[0]['returnAmount'])))
        T_amount=input('\n输入退货数量(小于等于可退数量)\n'.encode('gb18030'))
        back_res=newSession.post(url=back_url,data={'detailId':new_detail[0]['detailId'],'branchOrderId':data[0],'goodId':new_detail[0]['GoodId'],
                                                    'backGoodId':new_detail[0]['GoodId'],'orderId':orderId,'produceDates[]':time.strftime('%Y-%m-%d',time.localtime(time.time())),
                                                    'amounts[]':int(T_amount),'onSellGoodsCombId':new_detail[0]['OnSellGoodsCombId'],'message':'','onSellGoodId':new_detail[0]['OnSellGoodId'],
                                                    'orderComboType':0,'backPackType':1,'backComboType':2})
        print('退货成功')
    else:
        for nd in new_detail:
            print('上架名称:',nd['sellName'],'\t库存名称:',nd['name'],'\t库存编号:',nd['OnSellGoodId'],'\t可退数量:',str(int(nd['amount'])-int(nd['returnAmount'])))
        T_order = input('\n输入要退的库存编号:\n'.encode('gb18030'))
        T_amount= input('\n输入退货数量(小于等于可退数量)\n'.encode('gb18030'))
        for nd in new_detail:
            if str(nd['OnSellGoodId'])==T_order:
                back_res = newSession.post(url=back_url,
                                           data={'detailId': nd['detailId'], 'branchOrderId': data[0],
                                                 'goodId': nd['GoodId'],
                                                 'backGoodId': nd['GoodId'], 'orderId': orderId,
                                                 'produceDates[]': time.strftime('%Y-%m-%d',
                                                                                 time.localtime(time.time())),
                                                 'amounts[]': int(T_amount),
                                                 'onSellGoodsCombId': nd['OnSellGoodsCombId'], 'message': '',
                                                 'onSellGoodId': nd['OnSellGoodId'],
                                                 'orderComboType': 0, 'backPackType': 1, 'backComboType': 2})
                print('退货成功')
                break


def SureOrder(cityId, agencyId, service_url, service_username, service_password):
    start = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    end = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 60 * 60))
    # 登陆客服
    newSession = requests.Session()
    service_login = '{0}/service/api/manager/login'.format(service_url)
    service_response = newSession.post(url=service_login,
                                       data={'account': service_username, 'password': service_password})
    # 切换城市
    service_changecity_url = '{0}/service/api/manager/updateAgency'.format(service_url)
    service_changecity_response = newSession.post(url=service_changecity_url,
                                                  data={'cityId': cityId, 'agencyId': agencyId})
    # 查看当前订单
    check_url = '{0}/service/api/order/list?offset=0&limit=1000&payType=1&order=store&start={1}%2000:00:00&end={2}%2000:00:00&message=0&timeTag=0'.format(
        service_url, start, end)
    check_url_response = newSession.get(url=check_url)
    check_json = json.loads(changeIntoStr(check_url_response.text))

    try:
        for cj in check_json['stores'][0]['orders']:
            if cj['state'] == 0:
                # 确认订单
                order_url = '{0}/service/api/order/send'.format(service_url)
                newSession.post(url=order_url, data={'orderId': int(cj['id'])})
                print('\n订单号:%s\t 审核通过\n' % cj['id'])
                return cj['id']
    except Exception as e:
        pass
# CancleOrder(320700,171,'http://192.168.1.251:3586','12345678910','123456','11116511')
SureOrder(320700,171,'http://192.168.1.251:3586','12345678910','123456','11116511')