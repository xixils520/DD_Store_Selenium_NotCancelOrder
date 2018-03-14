#coding:utf-8
from bs4 import BeautifulSoup
import os
import time
def getZengId(html):
    bs=BeautifulSoup(html,'lxml')
    div=bs.find('div',attrs={'class':'cart-good-element','id':False})
    if div:
        ZId = int(div.find('div',class_='cart-good-info-name').a['href'].split('=')[1])
        ZCount =int(div.find('div',class_='good-amount-wrapper fl-l').string)
    else:
        ZId=0
        ZCount=0
    return ZId,ZCount


def getPath(case_name):
    path = os.path.dirname(os.getcwd()) + '\\ScreenShot\\' + case_name+'_'+str(int(time.time()*1000)) + '.png'
    return path


def getFinalMoney(html):
    bs=BeautifulSoup(html,'lxml')
    if bs.find('span',id='final_price'):
        final_price=bs.find('span',id='final_price').string
        return float(final_price)


def getLoginStatus(html):
    bs=BeautifulSoup(html,'lxml')
    status=bs.find('a',attrs={'class':'NSimSun','href':'/login/off'})
    return status