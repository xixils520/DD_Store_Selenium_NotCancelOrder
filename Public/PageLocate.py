#coding:utf-8
from Public.BaseObject import Base
from selenium.webdriver.common.by import  By
import time
class elementLocate(Base):
    def __init__(self,driver,Locate_element):
        super(elementLocate,self).__init__(driver)
        self.Locate_element=Locate_element

    def findElementByXpath(self):
        ele_Tuple=(By.XPATH,self.Locate_element)
        return self.find_element(*ele_Tuple)

    def clickElementByXpath(self):
        ele_Tuple=(By.XPATH,self.Locate_element)
        self.find_element(*ele_Tuple).click()
        time.sleep(3)

    def findElementsByXpath(self):
        ele_Tuple=(By.XPATH,self.Locate_element)
        return self.find_elements(*ele_Tuple)


    def clickElementsByXpath(self,index):
        ele_Tuple=(By.XPATH,self.Locate_element)
        self.find_elements(*ele_Tuple)[index].click()
        time.sleep(3)

    def sendKeysElementByXpath(self,value):
        ele_Tuple=(By.XPATH, self.Locate_element)
        self.find_element(*ele_Tuple).send_keys(value)
        time.sleep(1)

