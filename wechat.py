#!/usr/bin/python
#_*_coding:utf-8 _*_
import urllib.request
import json
import sys
import base64
import hashlib


def gettoken(corpid, corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    print(gettoken_url)
    try:
        token_file = urllib.request.urlopen(gettoken_url)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    print(token)
    return token


def senddata(access_token, user, subject, content):
    #with open('/usr/lib/zabbix/alertscripts/graph/bg.png', mode='rb') as f:
    #    png = f.read()
    #png_md5 = hashlib.md5()
    #png_64 = base64.b16encode(png)
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser": "@all",
        "toparty": "5修改群组id",
        "msgtype": "text",
        "agentid": "1000005修改应用id",
        "text": {
            "content": subject + '\n' + content
        },
        "safe": "0"
    }

    send_data = json.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_request = urllib.request.Request(send_url, send_data)
    response = json.loads(urllib.request.urlopen(send_request).read())
    print(str(response))


if __name__ == '__main__':
    user = str(sys.argv[1])
    subject = str(sys.argv[2])
    content = str(sys.argv[3])

    corpid = '修改id'
    corpsecret = '修改key'
    accesstoken = gettoken(corpid, corpsecret)
    senddata(accesstoken, user, subject, content)
