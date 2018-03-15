#coding:utf-8
# coding:utf-8
import time,unittest
from PreRandy.randyData import preConditionForTest
from Public.Super_Unittest import SuperUnit
from Public.PageLocate import elementLocate
from Public.ResolveHtml import getPath
from Public.ResolveHtml import getFinalMoney
from Public.ResolveHtml import getLoginStatus

class StoreActivityHeiKa(SuperUnit):
    """商城活动,达豆,黑卡商品以及组合活动"""
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
        """黑卡商品活动(总价超过满折活动)"""
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
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.heikaGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，黑卡商品价格100，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 300.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 300.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        time.sleep(2)

    def test_002(self):
        """黑卡商品,达豆活动(总价超过满折活动)"""
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
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.heikaGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        # 
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，黑卡商品价格100，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 290.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 290.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        time.sleep(2)

    def test_003(self):
        """黑卡商品,达豆活动,赠豆活动(总价超过满折活动)"""
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
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.heikaZendDouGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，黑卡商品价格100，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 275.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 275.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        time.sleep(2)

    def test_004(self):
        """黑卡商品,达豆活动,限时特价活动(原价120,现价100)(总价超过满折活动)"""
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
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.heikaTJGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，黑卡商品价格100，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 290.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 290.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)
        # 取消订单
        time.sleep(2)

if __name__=='__main__':
    unittest.main()