#coding:utf-8
import time,unittest,os
from PreRandy.randyData import preConditionForTest
from Public.Super_Unittest import SuperUnit
from Public.PageLocate import elementLocate
from Public.ResolveHtml import getPath
from Public.ResolveHtml import getFinalMoney
from Public.ResolveHtml import getLoginStatus
from Public.ResolveHtml import getZengId

class StoreActivityManZeng(SuperUnit):
    """商城活动,优惠卷,红包,达豆,满赠商品(满300赠)以及组合活动"""

    # def test_000(self):
    #     """数据准备"""
    #     #新建优惠券
    #     preConditionForTest().TestMysqlCoupon()
    #     #新建红包
    #     preConditionForTest().createNewRedGift()
    #     #取消客服所有订单
    #     #preConditionForTest().cancleOrderFromSQL()
    #     print('新建优惠券5元,新建红包10元,发放达豆数量1000，取消客服所有订单')
    def test_001(self):
        """满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!='无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 360.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 360.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)

    def test_002(self):
        """优惠券,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!='无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 355.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 355.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)

    def test_003(self):
        """红包,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 350.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 350.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)

    def test_004(self):
        """达豆,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!='无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 350.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 350.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)

    def test_005(self):
        """优惠卷,红包,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 345.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 345.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)

    def test_006(self):
        """优惠券,达豆,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!='无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 345.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 345.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)

    def test_007(self):
        """红包,达豆,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 340.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 340.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)

    def test_008(self):
        """满赠商品,优惠券,红包,达豆,满折(满200打8折)活动"""
        #满赠商品 所有活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        # getZGoodId,getZGoodIdCount=getZengId(self.driver.page_source)
        # print getZGoodId,getZGoodIdCount
        #
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，物品价格150，3件，各活动赠物品后打8折"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 335.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 335.0)
        # self.assertTrue(self.ZGoodId==getZGoodId)
        # self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        
        
        time.sleep(2)
if __name__=='__main__':
    unittest.main()