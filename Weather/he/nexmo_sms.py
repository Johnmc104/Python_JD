#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys,urllib,urllib2,httplib,json

reload(sys)
sys.setdefaultencoding('utf-8') 

#查询
baseurl = 'https://free-api.heweather.com/v5/'
ikey = '1be15036695c4206b949a3c1ffc7ce72'

print ("Please tell us city name")
City_name = raw_input("Enter your city nmae: ")

url = str(baseurl) + 'search?city=' + str(City_name) + '&key=' + str(ikey)
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

#获取现在的天气、温度、体感温度、风向、风力等级
now_weather = data['now']['cond']['txt']
now_tmp = data['now']['tmp']
now_fl = data['now']['fl']
now_wind_dir = data['now']['wind']['dir']
now_wind_sc = data['now']['wind']['sc']

#今天的天气
today = data['daily_forecast'][0]
weather_day = today['cond']['txt_d']
weather_night = today['cond']['txt_n']
tmp_high = today['tmp']['max']
tmp_low = today['tmp']['min']
wind_dir = today['wind']['dir']
wind_sc = today['wind']['sc']

#天气建议

#舒适度
comf = data['suggestion']['comf']['brf']
comf_txt = data['suggestion']['comf']['txt']

#流感指数
flu = data['suggestion']['flu']['brf']
flu_txt = data['suggestion']['flu']['txt']

#穿衣指数
drsg = data['suggestion']['drsg']['brf']
drsg_txt = data['suggestion']['drsg']['txt']

w1 = "%s今天白天%s,夜间%s,现在%s,%s摄氏度." %(city,weather_day,weather_night,now_weather,now_tmp)
w2 = "今天最高%s度,最低%s度,PM2.5:%s,空气质量:%s." %(tmp_high,tmp_low,pm25,air_quality)
w3 = "%s,%s级." %(now_wind_dir,now_wind_sc)
w4 = "天气舒适度：%s,%s." %(comf,comf_txt)
w5 = "穿衣指数：%s,%s." %(drsg,drsg_txt)
w6 = "流感指数：%s,%s. " %(flu,flu_txt)

print (w1)
print (w2)
print (w3)
print (w4)
print (w5)
print (w6)

mes = w1 + w2

import urllib
import urllib2

params = {
    'api_key': '0dab49b6',
    'api_secret': 'd8e0ac6465921067',
    'to': '8615061826156',
    'from': '441632960961',
    'text': mes
}

send_url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

request = urllib2.Request(send_url)
request.add_header('Accept', 'application/json')
response = urllib2.urlopen(request)


import json

#Using the response object from the request

if response.code == 200 :
    data = response.read()
    #Decode JSON response from UTF-8
    decoded_response = json.loads(data.decode('utf-8'))
    # Check if your messages are succesful
    messages = decoded_response["messages"]
    for message in messages:
        if message["status"] == "0":
            print "success"
else :
    #Check the errors
    print "unexpected http {code} response from nexmo api". response.code
