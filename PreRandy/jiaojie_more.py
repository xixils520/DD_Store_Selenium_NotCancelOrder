#coding:utf-8
import requests
import urllib.request, urllib.error, urllib.parse
import json
from multiprocessing import Process,JoinableQueue
server_url='http://192.168.1.251:48000'
url_username='12345678910'
url_password='123456'
cityId='320100'
agencyId='101'
session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
login_url = '{0}/users/login'.format(server_url)
login_data = {'userName': url_username, 'password': url_password}
session.post(url=login_url, data=login_data, headers=headers)
# 切换城市
zdh_url = '{0}/users/updateAgency'.format(server_url)
zdh_data = {'cityId': cityId, 'agencyId': agencyId}
zdh_res=session.post(url=zdh_url, data=zdh_data, headers=headers)


def changeIntoStr(data,str_data=''):
    if isinstance(data, str):
        str_data = data.encode('utf-8')
    elif isinstance(data, str):
        str_data = data
    return str_data
class ThreadUrl(Process):
    def __init__(self, queue):
        super(ThreadUrl, self).__init__()
        self.queue = queue
        self.headers = {"User-Agent": "okhttp/3.8.0"}

    def run(self):
        while not self.queue.empty():
            orderId = self.queue.get()
            try:
                ps = 'ps001'
                courierId = 42
                name='11'
                reviewOrder_url = 'http://192.168.1.251:48000/api/stockOut/scan/reviewOrder?orderId={0}&courierId={1}&virtualCourierId={2}&courierName={3}'.format(
                    orderId, courierId, ps, urllib.parse.quote(name.encode('utf-8')))
                session.get(url=reviewOrder_url)
                confirm_Url = 'http://192.168.1.251:48000/api/stockOut/delivery/reviewConfirm'
                confirm_res = session.post(url=confirm_Url, data={'orderId': orderId, 'courierId': courierId})
                confirm_json = json.loads(changeIntoStr(confirm_res.text))
                if confirm_json['tag'] == 'success':
                    print('\n出库成功')
            except Exception as e:
                print(e)
            self.queue.task_done()
def main():
    queue=JoinableQueue()
    #11117358,11117356,11117355,11117354,11117353,11117352,11117351,11117350
    q=[11117358,11117356,11117355,11117354,11117353,11117352,11117351,11117350]
    for i in q:
        queue.put(i)
    for i in range(len(q)):
        t=ThreadUrl(queue)
        t.start()
    queue.join()
if __name__=='__main__':
    main()