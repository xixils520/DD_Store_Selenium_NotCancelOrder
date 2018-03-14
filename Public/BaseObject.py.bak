#coding:utf-8
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append (r'..')
from selenium.common.exceptions import NoSuchElementException,TimeoutException
class Base(object):
    def  __init__(self,driver):
        self.driver=driver

    def find_element(self,*element):
        try:
            time.sleep(1.5)
            self.driver.implicitly_wait(5)
            WebDriverWait(self.driver,12,1).until(lambda driver: driver.find_element(*element).is_displayed())
            WebDriverWait(self.driver,12,1).until(EC.presence_of_element_located(element))
            return self.driver.find_element(*element)
        except NoSuchElementException as e:
            print e
            time.sleep(3)
            self.driver.implicitly_wait(5)
            return self.driver.find_element(*element)


    def find_elements(self,*element):
        try:
            time.sleep(1.5)
            self.driver.implicitly_wait(5)
            WebDriverWait(self.driver,12,1).until(lambda driver: driver.find_element(*element).is_displayed())
            WebDriverWait(self.driver,12,1).until(EC.presence_of_element_located(element))
            return self.driver.find_elements(*element)
        except NoSuchElementException as e:
            print e
            time.sleep(3)
            self.driver.implicitly_wait(5)
            return self.driver.find_elements(*element)
        except TimeoutException as e:
            print e
            self.driver.implicitly_wait(5)
            return self.driver.find_elements(*element)

    def do_swipe(self,direction):
        window = self.driver.get_window_size()
        width = int(window[u'width'])
        height = int(window[u'height'])
        switcher={
            "up":lambda :self.driver.swipe(width /2, height * 3/4, width /2, height * 1/4, 1000),
            "down":lambda :self.driver.swipe(width / 2, height * 1 / 4, width / 2, height * 3 / 4, 1000),
            "left":lambda :self.driver.swipe(width * 5 / 6, height / 2, width * 1 / 6, height / 2, 1000),
            "right":lambda :self.driver.swipe(width * 1 / 6, height / 2, width * 5 / 6, height / 2, 1000)}
        return switcher.get(direction)()





