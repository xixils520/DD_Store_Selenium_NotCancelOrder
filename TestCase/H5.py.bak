#coding:utf-8
# coding:utf-8
import time,unittest,os
from PreRandy.randyData import preConditionForTest
from Public.Super_Unittest import SuperUnit
from Public.PageLocate import elementLocate
from bs4 import BeautifulSoup
class StoreActivity(SuperUnit):
    """店达商城活动测试"""
    #全局信息
    #满200打8折
    mainGoodId=125767  #价格75,无活动
    zengDouGoodId=125801  #价格80，赠豆4元
    manJianGoodId=125802   #价格100 ，满50减10
    manZengGoodId=125804   #价格150 ，赠125805 一个
    ZGoodId=125805     #满300赠的非卖品
    ZGoodIdCount = 1 # 满300赠的非卖品
    heikaGoodId=125811   #价格100 ，黑卡活动，除了赠豆不享受其他优惠
    weihuoGoodId=125822  #价格30，尾货闪销

    def test_000(self):
        """数据准备"""
        #新建优惠券
        #preConditionForTest().TestMysqlCoupon()
        #新建红包
        #preConditionForTest().createNewRedGift()
        #取消客服所有订单
        preConditionForTest().cancleOrderFromSQL()
        print u'新建优惠券5元,新建红包10元,发放达豆数量1000，取消客服所有订单'
    def test_001(self):
        """测试优惠券"""
        # 测试优惠券
        #只允许出现优惠券
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='list_info']/div/div[2]").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 70.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 70.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_002(self):
        """测试红包"""
        # 测试红包
        # 只允许使用红包
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 65.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 65.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_003(self):
        """测试达豆"""
        #测试达豆
        #只允许使用达豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件，达豆减3.5"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 71.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 71.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)

        #取消订单
        preConditionForTest().cancleOrder()

    def test_004(self):
        """测试赠豆"""
        #测试赠豆
        #只允许赠豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件，赠豆减4元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 76.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 76.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_005(self):
        """满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 90.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 90.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)

        #取消订单
        preConditionForTest().cancleOrder()
    def test_006(self):
        """满折活动,满200打8折"""
        #满折活动  #商品
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
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
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折后180"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 180.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 180.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)

        #取消订单
        preConditionForTest().cancleOrder()
    def test_007(self):
        """满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
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
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 360.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 360.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)

        #取消订单
        preConditionForTest().cancleOrder()
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
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，各活动赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 335.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 335.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        # 取消订单
        preConditionForTest().cancleOrder()

    def test_009(self):
        """满减商品(满50减10),优惠券,红包,达豆,满折(满200打8折)活动"""
        # 满减商品 所有活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，3件，各活动满减后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 207.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 207.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)

        # 取消订单
        preConditionForTest().cancleOrder()

    def test_010(self):
        """黑卡商品，达豆活动"""
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.heikaGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，黑卡商品价格100，3件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 290.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 290.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        # 取消订单
        preConditionForTest().cancleOrder()

    def test_011(self):
        """尾货闪销，达豆活动"""
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.weihuoGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，尾货商品上架60，活动价格30，3件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 85.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 85.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        elementLocate(self.driver,".//div[2]/div[2]/div[3]/button[2]").clickElementByXpath()
        time.sleep(3)
        # 取消订单
        preConditionForTest().cancleOrder()

    def test_012(self):
        """测试优惠券,红包组合"""
        # 测试优惠券
        #只允许出现优惠券，红包
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 60.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 60.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_013(self):
        """测试优惠券,达豆组合"""
        # 测试优惠券
        #只允许出现优惠券，达豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='list_info']/div/div[2]").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 66.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 66.5)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_014(self):
        """测试红包,达豆组合"""
        # 测试优惠券
        #只允许出现优惠券，达豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 62.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 62.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_015(self):
        """测试优惠券,达豆组合"""
        # 测试优惠券
        #只允许出现优惠券，达豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='list_info']/div/div[2]").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 66.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 66.5)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()


    def test_016(self):
        """测试优惠券,红包,达豆组合"""
        # 测试优惠券
        #只允许出现优惠券，达豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 57.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 57.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_017(self):
        """测试优惠券,赠豆组合"""
        # 测试优惠券
        #只允许出现优惠券，达豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='list_info']/div/div[2]").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 71.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 71.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_018(self):
        """测试红包,赠豆组合"""
        # 测试优惠券
        #只允许出现红包，赠豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 66.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 66.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_019(self):
        """测试达豆,赠豆组合"""
        # 测试优惠券
        #只允许达豆，赠豆
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 72.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 72.5)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_020(self):
        """测试优惠券,红包,赠豆组合"""
        # 测试优惠券
        #只允许优惠券,红包,赠豆组合
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 61.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 61.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_021(self):
        """测试红包,达豆,赠豆组合"""
        # 测试优惠券
        #只允许红包,达豆,赠豆组合
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,1000)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 63.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 63.0)
        elementLocate(self.driver,".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_022(self):
        """测试优惠券,达豆,赠豆组合"""
        # 测试优惠券
        # 只允许优惠券,达豆,赠豆组合"
        # 更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        # 清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")

        current_money = getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件"
        print self._testMethodName, current_money
        # TODO 需要加入金额断言
        if current_money != 67.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 67.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        # 取消订单
        preConditionForTest().cancleOrder()

    def test_023(self):
        """测试优惠券,红包,达豆,赠豆组合"""
        # 测试优惠券
        # 只允许优惠券,红包,达豆,赠豆组合
        # 更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        # 清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.zengDouGoodId))
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money = getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格80，1件"
        print self._testMethodName, current_money
        # TODO 需要加入金额断言
        if current_money != 58.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 58.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        # 取消订单
        preConditionForTest().cancleOrder()

    def test_024(self):
        """优惠券,满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 85.0:
            self.screenShot(getPath(self._testMethodName))

        self.assertTrue(current_money == 85.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)

        #取消订单
        preConditionForTest().cancleOrder()
    def test_025(self):
        """红包,满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 80.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 80.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_026(self):
        """达豆,满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 85.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 85.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_027(self):
        """优惠券，红包，满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 75.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money ==75.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()

    def test_028(self):
        """优惠券，达豆，满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,500)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 81.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 81.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_029(self):
        """红包，达豆，满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 76.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 76.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_030(self):
        """优惠券，红包，达豆，满减活动,满50减10"""
        #满减活动 #全局活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manJianGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格100，1件，减10元"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 71.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 71.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_031(self):
        """优惠券,满折活动,满200打8折"""
        #满折活动
        #商品  优惠券,满折活动,满200打8折
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 175.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 175.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_032(self):
        """红包,满折活动,满200打8折"""
        #满折活动  #商品
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
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

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 170.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 170.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_033(self):
        """达豆,满折活动,满200打8折"""
        #满折活动  #商品
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
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
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折后180"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 171.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 171.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_034(self):
        """优惠券,红包,满折活动,满200打8折"""
        #满折活动  #商品
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 165.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 165.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_035(self):
        """优惠券,达豆,满折活动,满200打8折"""
        #满折活动  #商品
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 166.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 166.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_036(self):
        """红包,达豆,满折活动,满200打8折"""
        #满折活动  #商品
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='code_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='code_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='code_list']/div[1]/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,700)")

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 161.5:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 161.5)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_037(self):
        """优惠券,达豆,红包,满折活动,满200打8折"""
        #满折活动  #商品
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.mainGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()

        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格75，3件，打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 157.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 157.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_038(self):
        """优惠券,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 355.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 355.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_039(self):
        """红包,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
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
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 350.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 350.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_040(self):
        """达豆,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
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
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 350.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 350.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_041(self):
        """优惠卷,红包,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
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
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 345.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 345.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_042(self):
        """优惠券,达豆,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.manZengGoodId))
        elementLocate(self.driver,".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='cash_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='cash_amount']").findElementByXpath().text!=u'无可用红包':
            elementLocate(self.driver,".//*[@id='cash_list']/div/div[1]/div/input").clickElementByXpath()
        self.driver.execute_script("window.scrollBy(0,300)")
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 345.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 345.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_043(self):
        """红包,达豆,满赠活动,满300赠,满折(满200打8折)"""
        #满赠活动
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
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
        getZGoodId,getZGoodIdCount=zengGoodId(self.driver.page_source)
        print getZGoodId,getZGoodIdCount
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，物品价格150，3件，赠物品后打8折"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 340.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 340.0)
        self.assertTrue(self.ZGoodId==getZGoodId)
        self.assertTrue(self.ZGoodIdCount==getZGoodIdCount)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        #取消订单
        preConditionForTest().cancleOrder()
    def test_044(self):
        """黑卡商品活动(总价超过满折活动)"""
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
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
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，黑卡商品价格100，3件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 300.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 300.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        time.sleep(3)
        # 取消订单
        preConditionForTest().cancleOrder()

    def test_045(self):
        """尾货闪销活动(总价超过满折活动)"""
        #更改达豆数量
        preConditionForTest().UpdateTestUserDadou()
        #清空购物车
        preConditionForTest().clean_redis()
        self.openUrl('http://192.168.1.251:30011/login')
        time.sleep(3)
        if not getLoginStatus(self.driver.page_source):
            elementLocate(self.driver, ".//*[@id='uid']").sendKeysElementByXpath('13262860621')
            elementLocate(self.driver, ".//*[@id='pwd']").sendKeysElementByXpath('123456')
            elementLocate(self.driver, ".//*[@id='login_submit']").clickElementByXpath()
        self.openUrl('http://192.168.1.251:30011/detail?gid={0}'.format(self.weihuoGoodId))
        for s in range(7):
            elementLocate(self.driver, ".//div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='link_cart']").clickElementByXpath()
        elementLocate(self.driver, ".//*[@id='total']/div[2]/button").clickElementByXpath()
        elementLocate(self.driver,".//*[@id='dadou_toggle_button']").clickElementByXpath()
        if elementLocate(self.driver,".//*[@id='dadou_no']").findElementByXpath().text!='0':
            elementLocate(self.driver,".//*[@id='dadou_check']").clickElementByXpath()
        current_money=getFinalMoney(self.driver.page_source)
        print u"购物车，尾货商品上架60，活动价格30，7件"
        print self._testMethodName,current_money
        # TODO 需要加入金额断言
        if current_money != 210.0:
            self.screenShot(getPath(self._testMethodName))
        self.assertTrue(current_money == 210.0)
        elementLocate(self.driver, ".//*[@id='checkout_button']/button").clickElementByXpath()
        elementLocate(self.driver,".//div[2]/div[2]/div[3]/button[2]").clickElementByXpath()
        time.sleep(3)
        # 取消订单
        preConditionForTest().cancleOrder()


def zengGoodId(html):
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

if __name__=='__main__':
    unittest .main()