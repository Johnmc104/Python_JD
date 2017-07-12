# -*- coding: utf-8 -*-
import sys
import httplib
import urllib2
import json
import time
from mns.account import Account
from mns.queue import *
from mns.topic import *
from mns.subscription import *
import ConfigParser

#获取配置信息
accessKeyId =  ""
accessKeySecret =  ""
endpoint = " "
securityToken = ""


#初始化my_account
my_account = Account("", "", "")
my_queue = my_account.get_queue("MyQueue-%s" % time.strftime("%y%m%d-%H%M%S", time.localtime()))
my_topic = my_account.get_topic("sms.topic-cn-shanghai")

'''
天气查询
'''
reload(sys)
sys.setdefaultencoding('utf-8')

#查询城市ID
baseurl = 'https://free-api.heweather.com/v5/'
ikey = '1be15036695c4206b949a3c1ffc7ce72'

print ("Please tell us city name")
city_n = raw_input("Enter your city nmae: ")

url = str(baseurl) + 'search?city=' + str(city_n) + '&key=' + str(ikey)
id_req = urllib2.Request(url)
id_resp = urllib2.urlopen(id_req).read()

#将JSON转化为Python的数据结构
id_json_data = json.loads(id_resp)
id_data = id_json_data['HeWeather5'][0]

#获取城市id的值
cityid = id_data['basic']['id']

all_url = str(baseurl) + 'weather?city=' + str(cityid) + '&key=' + str(ikey)
req = urllib2.Request(all_url)
resp = urllib2.urlopen(req).read()

#将JSON转化为Python的数据结构
json_data = json.loads(resp)
data = json_data['HeWeather5'][0]

#获取PM2.5的值
pm25 = data['aqi']['city']['pm25']
#获取空气质量
air_quality = data['aqi']['city']['qlty']

#获取城市
city = data['basic']['city']
print "We are inquiring about the weather in %s for you" % city

#今天的天气
today = data['daily_forecast'][0]
weather_day = today['cond']['txt_d']
weather_night = today['cond']['txt_n']
tmp_high = today['tmp']['max']
tmp_low = today['tmp']['min']
wind_dir = today['wind']['dir']
wind_sc = today['wind']['sc']

'''
生成SMS消息属性，single=True表示每个接收者参数一样
'''
#设置SMSSignName（签名）和SMSTempateCode（模板ID）
direct_sms_attr = DirectSMSInfo(free_sign_name="SMSSignName", template_code="SMSTempateCode", single=True)
#指定接收短信的手机号并指定发送给该接收人的短信中的参数值（在短信模板中定义的）
direct_sms_attr.add_receiver(receiver="138xxx")
#设置参数值，多个参数用,隔开（注意中文英文符号区别）
direct_sms_attr.set_params({"name": "", "city": city, })


'''
生成SMS消息对象
'''
msg_body = "I am test message."
msg1 = TopicMessage(msg_body, direct_sms = direct_sms_attr)


try:
    '''
    发布SMS消息
    '''
    re_msg = my_topic.publish_message(msg1)
    print "Publish Message Succeed. MessageBody:%s MessageID:%s" % (msg_body, re_msg.message_id)
except MNSExceptionBase,e:
    if e.type == "TopicNotExist":
        print "Topic not exist, please create it."
        sys.exit(1)
    print "Publish Message Fail. Exception:%s" % e
