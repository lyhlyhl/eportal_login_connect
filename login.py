import requests
import json
from urllib import parse
import time
url_login = "http://10.254.241.19/eportal/InterFace.do?method=login"
url_getOnlineUserInfo = "http://10.254.241.19/eportal/InterFace.do?method=getOnlineUserInfo"
url_getservices = "http://10.254.241.19/eportal/InterFace.do?method=getServices&queryString="

userId = ""
password = ""
serveName = "校园网" #校园网 联通 电信 移动

data_serve = {
    'queryString':""
}
data_login = {
    'userId' : userId,
    'password':password,
    'queryString':"",
    'service':"",
    'operatorPwd':"",
    'operatorUserId':"",
    'validcode':"",
    'passwordEncrypt':"false"
}

def getImformation(service):
    imformation = requests.get("http://10.254.241.19/")
    imformation = imformation.text.split("'")[1]
    imformation = parse.quote(imformation.split("?")[1],encoding='utf-8')
    print(1)
    data_login['queryString'] = imformation
    data_serve['queryString']=imformation
    data_login['service']=parse.quote(service)

def loginAndTest():
    flag = 0
    s = requests.session()
    b_time = 0
    while(1):
        if flag == 1:
            print("try to connect!")
            r = s.post(url_login, data=data_login)
            r = json.loads(r.content)
            print(r)
            if r['result'] == "fail":
                pass
            else:
                print("Success!")
                flag = 0
        a_time = time.time()
        if a_time - b_time > 60:
            print(a_time - b_time)
            b_time = time.time()
            OnlineStatus = s.get(url_getOnlineUserInfo)
            data = json.loads(OnlineStatus.text)
            if data['result'] != 'wait':
                print("Not login")
                flag = 1
            else:
                print("Everything is Ok!")
if __name__ == '__main__':
    getImformation(serveName)
    loginAndTest()


