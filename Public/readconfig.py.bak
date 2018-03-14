#coding:utf-8
import ConfigParser
import os
import shutil
fileJudge=os.path.dirname(os.getcwd())

def readAppConfig(tag_session,tag_info):
    config = ConfigParser.ConfigParser()
    with open(fileJudge+'\\Settings\\'+tag_session,"r") as cfgfile:
        config.readfp(cfgfile)
        appName = config.get(tag_info, 'appName')
        activityName=config.get(tag_info,"activityName")
    return appName,activityName

def readScheduleConfig():
    config = ConfigParser.ConfigParser()
    with open(fileJudge+"\\Settings\\config.ini","r") as cfgfile:
        config.readfp(cfgfile)
        start_minute=config.get("time","start_minute")
        start_hour=config.get("time","start_hour")
    return start_minute,start_hour

def removeall(rootdir):
    filelist=os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join( rootdir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
            print (filepath+" removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)
            print ("dir "+filepath+" removed!")


if __name__=="__main__":
    print readAppConfig('appiumInfo.ini','FlWareHouse')
    # print device_info