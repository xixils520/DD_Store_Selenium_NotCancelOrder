#coding:utf-8
# coding:utf-8
import time,unittest
from PreRandy.randyData import preConditionForTest
from Public.Super_Unittest import SuperUnit
from Public.PageLocate import elementLocate
from Public.ResolveHtml import getPath
from Public.ResolveHtml import getFinalMoney
from Public.ResolveHtml import getLoginStatus

class StoreActivityThird(SuperUnit):
    """商城活动,第三方满减,满赠,红包以及组合活动"""
    def test_001(self):
        """第三方红包活动"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text!='已领取':
            elementLocate(self.driver,".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.normalThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，第三方满减商品价格80，1件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 64.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 64.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

    def test_002(self):
        """第三方满减商品活动_无梯度(满50减10)活动"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,
                         ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text != '已领取':
            elementLocate(self.driver, ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='list_info']/div/div[2]").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，第三方满减商品价格80，1件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 69.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 69.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

    def test_003(self):
        """第三方满减商品活动_无梯度(满50减10),红包组合活动"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,
                         ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text != '已领取':
            elementLocate(self.driver, ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，第三方满减商品价格80，1件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 64.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 64.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

    def test_004(self):
        """第三方满减商品活动第一梯度(满100减20,200减20,300减40),红包组合活动"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,
                         ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text != '已领取':
            elementLocate(self.driver, ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianTDThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，价格100，多梯度满减 满100减10，满200减20，满300减40，1件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 84.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 84.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

    def test_005(self):
        """第三方满减商品活动第二梯度(满100减20,200减20,300减40),红包组合活动"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,
                         ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text != '已领取':
            elementLocate(self.driver, ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianTDThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，价格100，多梯度满减 满100减10，满200减20，满300减40，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 173.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 173.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

    def test_006(self):
        """第三方满减商品活动第三梯度(满100减20,200减20,300减40),红包组合活动"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,
                         ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text != '已领取':
            elementLocate(self.driver, ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianTDThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，价格100，多梯度满减 满100减10，满200减20，满300减40，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 252.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 252.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

    def test_007(self):
        """第三方满赠商品活动(满250赠)"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,
                         ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text != '已领取':
            elementLocate(self.driver, ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='list_info']/div/div[2]").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")

        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，黑卡商品价格100，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 298.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 298.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

    def test_008(self):
        """第三方满赠商品活动(满250赠),红包组合活动"""
        
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath(self.store_username)
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/activity/third?id=')
        if elementLocate(self.driver,
                         ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").findElementByXpath().text != '已领取':
            elementLocate(self.driver, ".//div[4]/div/div[2]/ul/div/div[1]/div/div[3]").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengThirdGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[6]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        # current_money=getFinalMoney(self.driver.page_source)
        # print u"购物车，黑卡商品价格100，3件"
        # print self._testMethodName,current_money
        # # TODO 需要加入金额断言
        # if current_money != 293.0:
        #     self.screenShot(getPath(self._testMethodName))
        # self.assertTrue(current_money == 293.0)
        elementLocate(self.driver, ".//*[@id='cart_preview']/div[7]/div/div[1]").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(2)

if __name__=='__main__':
    unittest.main()