#coding:utf-8
import requests,time
from io import BytesIO
class global_system():
    def __init__(self):
        self.global_url='http://192.168.1.251:39000'
        self.session = requests.session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    def main(self):
        while True:
            print("可批量添加商品，以逗号分割商品名！")
            run = int(eval(input("\n\t\t1.运行\t2.退出\n")))
            if run == 1:
                names = eval(input('输入商品名：'))
                names = names.replace("，" , ",")
                for name in names.split(','):
                    back = self.create_product(name)
                    run1 = int(eval(input('\n1.绑定整装\n2.退出\n')))
                    if run1 == 1:
                        self.create_full_product(name,back)
                    elif run1 == 2:
                        break
            elif run == 2:
                break

    def create_product(self,name):
        # 登录全局系统
        login_data = {
            'userName' : 12345678910,
            'password' : 123456
        }
        login = self.session.post(url=self.global_url + '/users/login',data=login_data,headers = self.headers)
        # 添加商品
        add_data = {
            'brandId':'2436',
            'country':'中国',
            'name': name + '_' + str(int((time.time()))),
            'catalog':['0','4090100','2'],
            'packType':'0',
            'barCode':'123456',
            'catalogId':'4090100',
            'specification':'12瓶/箱',
            'unit':'1',
            'tax':'17',
            'length':'1',
            'width':'1',
            'height':'1',
            'volume':'1.00',
            'weight':'1',
            'termOfValidity':'180',
            'timeUnit':'2',
            'transProportion':'1',
            'introduction':'<p>test</p>',
        }
        add_product = self.session.post(url=self.global_url + '/goods/add', data=add_data, headers=self.headers)
        # 提取库存编号
        goods_list = self.session.post(url=self.global_url + '/goods/list/Json',data={'draw': '1', 'columns[0][data]': 'id', 'columns[0][searchable]': 'true', 'columns[0][orderable]': 'true', 'columns[0][search][regex]': 'false', 'columns[1][data]': 'name', 'columns[1][searchable]': 'true', 'columns[1][orderable]': 'true', 'columns[1][search][regex]': 'false', 'columns[2][data]': 'brand', 'columns[2][searchable]': 'true', 'columns[2][orderable]': 'true', 'columns[2][search][regex]': 'false', 'columns[3][data]': 'state', 'columns[3][searchable]': 'true', 'columns[3][orderable]': 'false', 'columns[3][search][regex]': 'false', 'columns[4][data]': 'customCode', 'columns[4][searchable]': 'false', 'columns[4][orderable]': 'false', 'columns[4][search][regex]': 'false', 'columns[5][data]': 'packType', 'columns[5][searchable]': 'false', 'columns[5][orderable]': 'false', 'columns[5][search][regex]': 'false', 'columns[6][searchable]': 'false', 'columns[6][orderable]': 'false', 'columns[6][search][regex]': 'false', 'columns[7][data]': 'specification', 'columns[7][searchable]': 'false', 'columns[7][orderable]': 'false', 'columns[7][search][regex]': 'false', 'columns[8][data]': 'unit', 'columns[8][searchable]': 'false', 'columns[8][orderable]': 'false', 'columns[8][search][regex]': 'false', 'columns[9][data]': 'termOfValidity', 'columns[9][searchable]': 'true', 'columns[9][orderable]': 'true', 'columns[9][search][regex]': 'false', 'columns[10][data]': 'tax_rate', 'columns[10][searchable]': 'true', 'columns[10][orderable]': 'true', 'columns[10][search][regex]': 'false', 'columns[11][data]': 'country_name', 'columns[11][searchable]': 'true', 'columns[11][orderable]': 'false', 'columns[11][search][regex]': 'false', 'columns[12][data]': 'new_good_state', 'columns[12][searchable]': 'true', 'columns[12][orderable]': 'false', 'columns[12][search][regex]': 'false', 'columns[13][data]': 'catalog', 'columns[13][searchable]': 'false', 'columns[13][orderable]': 'false', 'columns[13][search][regex]': 'false', 'columns[14][searchable]': 'false', 'columns[14][orderable]': 'false', 'columns[14][search][regex]': 'false', 'order[0][column]': '0', 'order[0][dir]': 'desc', 'start': '0', 'length': '30', 'search[regex]': 'false'})
        goods_json = goods_list.json()
        for good_json in goods_json['data']:
            if add_data['name'] == good_json['name']:
                self.good_id = good_json['id']
                print(('商品名称:%s\t库存编号:%d'%(add_data['name'],self.good_id)))
                break
        # 提交新品图片处理
        submit_product = self.session.post(url=self.global_url + '/goods/submitImg',data={'id':self.good_id},headers = self.headers)
        # 上传图片
        files_data = {
            'id':self.good_id,
            'imagePaths':-1,
            'images':'0'
        }
        img = requests.get('https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG/tam-ogel/b80a043c57da31ca37f99c22b53511e3_121_121.jpg')
        files_jpg = {'image0':('f',img.content,'image/jpeg')}
        print('正在上传图片....')
        commit_file = self.session.post(self.global_url + '/goods/addFile',data=files_data,files=files_jpg,headers = self.headers)
        return self.good_id

    def create_full_product(self,name,good_id):
        # 登录全局系统
        login_data = {
            'userName' : 12345678910,
            'password' : 123456
        }
        login = self.session.post(url=self.global_url + '/users/login',data=login_data,headers = self.headers)
        # 添加商品
        find = self.session.post(url = self.global_url + '/api/goods/findRelatedGoods',data={'id':good_id},headers = self.headers)
        find = find.json()
        add_data_full = {
         'brandId': '2436',
         'country': '中国',
         'name':name + '（整）_' + str(int((time.time()))),
         "catalog": ['1090200', '2'],
         "catalogId": '1090200',
         'barCode':'123456',
         "specification": '12瓶/箱',
         'unit':'1',
         'tax':'17',
         'length':'1',
         'height':'1',
         'width':'1',
         'volume':'1.00',
         'weight':'1',
         'termOfValidity':'180',
         'timeUnit':'2',
         "transProportion": 5,
         "sid":find['data']['id'],
         "sGoodName":find['data']['name'],
         "goodId":find['data']['id'],
         "sSpecification":find['data']['specification'],
         "sCustomCode":find['data']['customCode'],
         "sUnit":1,
         'introduction': '<p>test</p>',
        }
        add_product = self.session.post(url=self.global_url + '/goods/add', data=add_data_full, headers=self.headers)
        # 提取库存编号
        goods_list = self.session.post(url=self.global_url + '/goods/list/Json',data={'draw': '1', 'columns[0][data]': 'id', 'columns[0][searchable]': 'true', 'columns[0][orderable]': 'true', 'columns[0][search][regex]': 'false', 'columns[1][data]': 'name', 'columns[1][searchable]': 'true', 'columns[1][orderable]': 'true', 'columns[1][search][regex]': 'false', 'columns[2][data]': 'brand', 'columns[2][searchable]': 'true', 'columns[2][orderable]': 'true', 'columns[2][search][regex]': 'false', 'columns[3][data]': 'state', 'columns[3][searchable]': 'true', 'columns[3][orderable]': 'false', 'columns[3][search][regex]': 'false', 'columns[4][data]': 'customCode', 'columns[4][searchable]': 'false', 'columns[4][orderable]': 'false', 'columns[4][search][regex]': 'false', 'columns[5][data]': 'packType', 'columns[5][searchable]': 'false', 'columns[5][orderable]': 'false', 'columns[5][search][regex]': 'false', 'columns[6][searchable]': 'false', 'columns[6][orderable]': 'false', 'columns[6][search][regex]': 'false', 'columns[7][data]': 'specification', 'columns[7][searchable]': 'false', 'columns[7][orderable]': 'false', 'columns[7][search][regex]': 'false', 'columns[8][data]': 'unit', 'columns[8][searchable]': 'false', 'columns[8][orderable]': 'false', 'columns[8][search][regex]': 'false', 'columns[9][data]': 'termOfValidity', 'columns[9][searchable]': 'true', 'columns[9][orderable]': 'true', 'columns[9][search][regex]': 'false', 'columns[10][data]': 'tax_rate', 'columns[10][searchable]': 'true', 'columns[10][orderable]': 'true', 'columns[10][search][regex]': 'false', 'columns[11][data]': 'country_name', 'columns[11][searchable]': 'true', 'columns[11][orderable]': 'false', 'columns[11][search][regex]': 'false', 'columns[12][data]': 'new_good_state', 'columns[12][searchable]': 'true', 'columns[12][orderable]': 'false', 'columns[12][search][regex]': 'false', 'columns[13][data]': 'catalog', 'columns[13][searchable]': 'false', 'columns[13][orderable]': 'false', 'columns[13][search][regex]': 'false', 'columns[14][searchable]': 'false', 'columns[14][orderable]': 'false', 'columns[14][search][regex]': 'false', 'order[0][column]': '0', 'order[0][dir]': 'desc', 'start': '0', 'length': '30', 'search[regex]': 'false'})
        goods_json = goods_list.json()
        for good_json in goods_json['data']:
            if add_data_full['name'] == good_json['name']:
                self.good_id = good_json['id']
                print(('商品名称:%s\t库存编号:%d'%(add_data_full['name'],self.good_id)))
                break
        # 提交新品图片处理
        submit_product = self.session.post(url=self.global_url + '/goods/submitImg',data={'id':self.good_id},headers = self.headers)
        # 上传图片
        files_data = {
            'id':self.good_id,
            'imagePaths':-1,
            'images':'0'
        }
        img = requests.get('https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG/tam-ogel/b80a043c57da31ca37f99c22b53511e3_121_121.jpg')
        files_jpg = {'image0':('f',img.content,'image/jpeg')}
        print('正在上传图片....')
        commit_file = self.session.post(self.global_url + '/goods/addFile',data=files_data,files=files_jpg,headers = self.headers)

if __name__=='__main__':
    global_os = global_system()
    global_os.main()