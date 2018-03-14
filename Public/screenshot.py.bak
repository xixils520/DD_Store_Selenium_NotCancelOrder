#coding:utf-8

from time import strftime
from time import sleep
from PIL import Image
import os
import time
import  xlrd
from xlutils.copy import copy
import write_represult
import processfile

class defpath(object):
    work_path1=os.path.dirname(os.getcwd())+"\\result\\excel\\"
    excelfile="FailureReport.xls"

class screenshot(object):
    sss=defpath.work_path1
    #进行截图操作，并指定截图的范围 box为指定的起始坐标
    def screencap(self,workpath,driver,work_path1=defpath.work_path1,box=(0,0,1080,1920),**kwargs):
        self.driver=driver
        self.workpath=workpath
        self.box=box
        dict1 = kwargs
        self.name = dict1['name']
        self.body = dict1['body']
#        screencap_time = strftime("%Y-%m-%d %H_%M_%S-")

        stime=time.strftime('%m%d%H%M',time.localtime(time.time()))

#        self.workpath=self.workpath+time.strftime('%Y-%m-%d',time.localtime(time.time()))+"/"
  #      print self.workpath
        #判断存放各个方法截图的路径文件夹存在不
        processfile.testdirexists(self.workpath)
        tempfile=self.workpath + self.name +'_'+stime+ '.png'
 #       print tempfile
        try:
            self.driver.get_screenshot_as_file(tempfile)
            sleep(5)
        except:
            print u"截图不成功"

        #将报failure的信息写到对应的excel文档中
        content=[self.name,"Fail",tempfile,self.body]

        #判断是否有result\excel的文件夹存在
        processfile.testdirexists(work_path1)

        #将截图路径和运行的类名写入到excel中
        write_represult.writefile(work_path1+defpath.excelfile,content)



        #截图完之后，再保存具体的大小
        image=Image.open(tempfile)
        newImage = image.crop(box)
        newImage.save(tempfile)


        return self.name+'_'+stime+'.png'
