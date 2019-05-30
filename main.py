# -*- coding: utf-8 -*-
import itchat
import urllib,urllib2,json
import sys,random

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

num = 6
url = 'http://www.tuling123.com/openapi/api'
arr = ["", "", "", "", ""]
replay = ["来喽", "干啥呀", "你好呀", "在呢", "到"]

@itchat.msg_register(itchat.content.TEXT)
def get_replay(msg):
    global num
    info = msg['Text']
    if info.startswith('胖雨'):
        if info == '胖雨':
            print "========>", info
            itchat.send(replay[random.randint(0,4)], msg['FromUserName'])
        else:    
            print "========>", info
            data = {
                u"key": arr[num/100],
                "info": info[2:],
                u"loc": "",
                "userid": 'wechat-rebot'
            }

            data = urllib.urlencode(data)
            url2 = urllib2.Request(url, data)
            response = urllib2.urlopen(url2)

            apicontent = response.read()
            s = json.loads(apicontent, encoding='utf-8')
            if s['code'] == 100000:
                itchat.send(s['text'], msg['FromUserName'])
                num = num + 1

itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run(debug=True)
