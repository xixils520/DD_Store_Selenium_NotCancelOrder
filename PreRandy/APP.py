#coding:utf-8
import  time,unittest
from appium import webdriver
class baseinfo(unittest.TestCase):
    def setUp(self):
        desired_cups={}
        desired_cups['platformName']='Android'
        desired_cups['platformVersion']='6.0'
        desired_cups['deviceName']='de19c676'
        desired_cups['appPackage']='com.ddinfo.flashman'
        desired_cups['appActivity']='com.ddinfo.flashman.activity.HelloActivity'
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cups)
        time.sleep(10)
    def tearDown(self):
        self.driver.quit()
    def test_01_click(self):
        self.driver.find_element_by_id('com.ddinfo.flashman:id/tv_menu_left').click()
        time.sleep(3)
        while True:
            try:
                self.driver.find_element_by_name('送达').click()
                self.driver.find_element_by_id('com.ddinfo.flashman:id/et_goods_code').send_keys(8)
                self.driver.find_element_by_name('确认').click()
            except:
                pass

if __name__=="__main__":
    unittest.main()