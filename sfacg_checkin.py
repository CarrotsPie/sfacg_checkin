import requests
import time
import uuid
import sys
import hashlib
import json
import os

nonce = "C7DC5CAD-31CF-4431-8635-B415B75BF4F3"
device_token = str(uuid.uuid4())
SALT = "FN_Q29XHVmfV3mYX"
headers = {
    'Host': 'api.sfacg.com',
    'accept-charset': 'UTF-8',
    'authorization': 'Basic YW5kcm9pZHVzZXI6MWEjJDUxLXl0Njk7KkFjdkBxeHE=',
    'accept': 'application/vnd.sfacg.api+json;version=1',
    'user-agent': f'boluobao/5.0.36(android;32)/H5/{device_token}/H5',
    'accept-encoding': 'gzip',
    'Content-Type': 'application/json; charset=UTF-8'
}
device_token = device_token.upper()

def md5_hex(input, case):
    m = hashlib.md5()
    m.update(input.encode())

    if case == 'Upper':
        return m.hexdigest().upper()
    else:
        return m.hexdigest()


def check(cookie):
    headers['cookie'] = cookie
    resp = requests.get('https://api.sfacg.com/user?', headers=headers).json()
    if (resp["status"]["httpCode"] == 200):
        nick_Name = resp['data']['nickName']
        # print(f"{nick_Name} cookie未失效")
        return True
    else:
        return False


def login(username, password):
    
    timestamp = int(time.time() * 1000)
    sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
    headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
    data = json.dumps(
        {"password": password, "shuMeiId": "", "username": username})
    url = "https://api.sfacg.com/sessions"
    resp = requests.post(url, headers=headers, data=data)
    if (resp.json()["status"]["httpCode"] == 200):
        cookie = requests.utils.dict_from_cookiejar(resp.cookies)
        return cookie[".SFCommunity"], cookie["session_APP"]
    else:
        return "", ""


exp = 0
couponNum = 0
fireCoin = 0


def checkin(cookie):
    global exp
    global couponNum
    global fireCoin
    
    timestamp = int(time.time() * 1000)
    sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
    headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
    headers["cookie"] = cookie
    Date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    signDate = json.dumps({"signDate": Date})
    ReadData = json.dumps(
        {"seconds": 3605, "readingDate": Date, "entityType": 2})
    ListenData = json.dumps(
        {"seconds": 3605, "readingDate": Date, "entityType": 3})
    for _ in range(3):
            
        timestamp = int(time.time() * 1000)
        sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
        headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
        resp = requests.put(
            "https://api.sfacg.com/user/newSignInfo", headers=headers, data=signDate).json()
        # print(resp)
        if('status' in resp and resp['status']['httpCode'] == 200):
            couponNum += resp['data'][0]['num']
            
        timestamp = int(time.time() * 1000)
        sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
        headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
        requests.put('https://api.sfacg.com/user/readingtime',
                     headers=headers, data=ListenData)
            
        timestamp = int(time.time() * 1000)
        sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
        headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
        requests.put('https://api.sfacg.com/user/readingtime',
                     headers=headers, data=ReadData)
        
        timestamp = int(time.time() * 1000)
        sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
        headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
        requests.post('https://api.sfacg.com/user/tasks/5',
                      headers=headers, data=ListenData)
        
        timestamp = int(time.time() * 1000)
        sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
        headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
        requests.post('https://api.sfacg.com/user/tasks/17',
                      headers=headers, data=ListenData)
        for _ in range(3):

            timestamp = int(time.time() * 1000)
            sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
            headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
            requests.put('https://api.sfacg.com/user/readingtime',
                         headers=headers, data=ListenData)
            time.sleep(0.5)
            
            timestamp = int(time.time() * 1000)
            sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
            headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
            resp = requests.put(
                'https://api.sfacg.com/user/tasks/5', headers=headers, data=ListenData).json()
            # print(resp)
            if(resp['status']['httpCode'] == 200):
                fireCoin += resp['data']['fireCoin']
                exp += resp['data']['exp']
            
            timestamp = int(time.time() * 1000)
            sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
            headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
            resp = requests.put(
                'https://api.sfacg.com/user/tasks/17', headers=headers, data='').json()
            # print(resp)
            if(resp['status']['httpCode'] == 200):
                fireCoin += resp['data']['fireCoin']
                exp += resp['data']['exp']
        url = "https://api.sfacg.com/user/tasks/21"
        requests.post(url, headers=headers).json()
        for _ in range(5):
            
            timestamp = int(time.time() * 1000)
            sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
            headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
            url = f"https://api.sfacg.com/user/advertisements?deviceToken={device_token}&page=0&size=20"
            requests.get(url, headers=headers).json()
            
            timestamp = int(time.time() * 1000)
            sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
            headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
            url = f"https://api.sfacg.com/user/tasks/21/advertisement?aid=43&deviceToken={device_token}"
            resp = requests.put(url, headers=headers,
                                data=json.dumps({"num": 1})).json()
            # url = f"https://api.sfacg.com/user/tasks?taskCategory=5&package=com.sfacg&deviceToken={device_token}&page=0&size=10"
            # requests.get(url, headers=headers).json()
            
            timestamp = int(time.time() * 1000)
            sign = md5_hex(f"{nonce}{timestamp}{device_token}{SALT}", 'Upper')
            headers['sfsecurity'] = f'nonce={nonce}&timestamp={timestamp}&devicetoken={device_token}&sign={sign}'
            resp = requests.put("https://api.sfacg.com/user/tasks/21",
                                headers=headers, data='').json()
            if(resp['status']['httpCode'] == 200):
                couponNum += resp['data']['couponNum']
        time.sleep(5)


def send_message_to_dingtalk(token, text):
    if (token == ""):
        return
    webhook = f'https://oapi.dingtalk.com/robot/send?access_token={token}'
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {
            "content": text
        }
    }
    message_json = json.dumps(message)
    requests.post(url=webhook, data=message_json, headers=header)


if __name__ == "__main__":
    SFCommunity = os.environ.get('SFCommunity')
    session_APP = os.environ.get('session_APP')
    dingTalkToken = os.environ.get('dingTalkToken')
    if (not check(f".SFCommunity={SFCommunity}; session_APP={session_APP}")):
        username = os.environ.get('username')
        password = os.environ.get('password')
        SFCommunity, session_APP = login(username, password)
        if (not check(f".SFCommunity={SFCommunity}; session_APP={session_APP}")):
            send_message_to_dingtalk(dingTalkToken, "登录失败")
            print("登录失败")
            sys.exit()
    checkin(f".SFCommunity={SFCommunity}; session_APP={session_APP}")
    send_message_to_dingtalk(
        dingTalkToken, f"签到成功 获得代券{couponNum}  金币{fireCoin}  经验{exp}")
    print(f"签到成功 获得代券{couponNum}  金币{fireCoin}  经验{exp}")
