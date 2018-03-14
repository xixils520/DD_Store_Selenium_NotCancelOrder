#coding:utf-8
import pytesseract
from PIL import Image
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
class GetImageDate(object):
    def m(self,name):
        image = Image.open(name)
        # 转化到灰度图
        image = image.convert('L')
        # 保存图像
        image.save(name)
        text = pytesseract.image_to_string(image,config=tessdata_dir_config,lang='eng')
        print(text.replace(' ',''))

GetImageDate().m('1233.png')