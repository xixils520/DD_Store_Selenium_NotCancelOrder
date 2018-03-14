#coding:utf-8
import json
import requests
import time
import logging
import hashlib
class PreForConditionData(object):
    """
    初始化信息
    """
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
        """
        cityId:连云港城市码
        """
        self.cityId=320700
        """
        store_url:商城地址
        store_main_username:商城主仓登录账号
        store_main_password:商城主仓登录密码
        store_pre_username:商城前置仓登录账号
        store_pre_password:商城前置仓登录密码
        """
        self.store_url='http://192.168.1.251:30011'
        self.store_main_username='13262860621'
        self.store_main_password='123456'
        self.store_pre_username = '13262860624'
        self.store_pre_password = '123456'

        """
        product_id:初始化上架编号
        """
        self.product_id=''
        """
        session:初始化session节点
        """
        self.session=requests.Session()
        """
        初始化log格式
        """
        logging.basicConfig(
                            level=logging.WARNING,
                            format='[%(asctime)s] [%(levelname)s] %(message)s',
                            datefmt='%Y_%m_%d %H:%M:%S',
        )
    @classmethod
    def changeIntoStr(cls,data,str_data=''):
        if isinstance(data, unicode):
            str_data = data.encode('utf-8')
        elif isinstance(data, str):
            str_data = data
        return str_data

    @classmethod
    def returnMd5(cls,pwd):
        md = hashlib.md5()
        md.update(pwd)
        return md.hexdigest()

    @staticmethod
    def createTime():
        """
        :return: 返回发放开始时间，发放结束时间，可使用开始时间，可使用结束时间
        """
        grantStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()- 1* 60 * 60))
        useStart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()- 2* 60 * 60))
        useEnd = grantEnd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 24 * 60 * 60))
        return grantStart, grantEnd, useStart, useEnd

    @staticmethod
    def createName():
        """
        :return:返回自动创建名字
        """
        couponName = u'自动测' + str(int(time.time()))
        return couponName

    def __str__(self):
        return u'初始化商城下单信息'