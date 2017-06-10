# -*- coding: utf-8 -*-
import sys,urllib2,json

reload(sys)
sys.setdefaultencoding('utf-8') 

#查询
baseurl = 'https://free-api.heweather.com/v5/'
ikey = '1be15036695c4206b949a3c1ffc7ce72'

print ("Please tell us city name")
City_name = raw_input("Enter your city nmae: ")

url = str(baseurl) + 'search?city=' + str(City_name) + '&key=' + str(ikey)
req = urllib2.Request(url)
resp = urllib2.urlopen(req).read()

#将JSON转化为Python的数据结构
json_data = json.loads(resp)
id_data = json_data['HeWeather5'][0]

#获取城市id的值
cityid = id_data['basic']['id']

all_url = str(baseurl) + 'weather?city=' + str(cityid) + '&key=' + str(ikey)

#将JSON转化为Python的数据结构
json_data = json.loads(resp)
data = json_data['HeWeather5'][0]

print(data)

