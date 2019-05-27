import itchat
import urllib,urllib2,json

@itchat.msg_register(itchat.content.TEXT)
def get_replay(msg):
    info = msg['Text'].encode('utf-8')
    url = 'http://www.tuling123.com/openapi/api'
    data = {
        u"key": "xxx",
        "info": info,
        u"loc": "",
        "userid": 'wechat-rebot'
    }

    data = urllib.urlencode(data)
    url2 = urllib2.Request(url, data)
    response = urllib2.urlopen(url2)

    apicontent = response.read()
    s = json.loads(apicontent, encoding='utf-8')
    print 's==',s
    if s['code'] == 100000:
        itchat.send(s['text'], msg['FromUserName'])

itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run(debug=True)