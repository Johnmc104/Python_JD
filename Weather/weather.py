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
id_req = urllib2.Request(url)
id_resp = urllib2.urlopen(id_req).read()

#将JSON转化为Python的数据结构
json_data = json.loads(id_resp)
id_data = json_data['HeWeather5'][0]

#获取城市id的值
cityid = id_data['basic']['id']


#查询天气数据
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


w1 = "%s今天白天天气%s,夜间天气%s,现在%s,%s摄氏度。" %(city,weather_day,weather_night,now_weather,now_tmp)
w2 = "最高气温%s摄氏度,最低气温%s摄氏度,PM2.5:%s,空气质量:%s。" %(tmp_high,tmp_low,pm25,air_quality)
w3 = "现在%s,%s级。" %(now_wind_dir,now_wind_sc)
w4 = "天气舒适度：%s,%s" %(comf,comf_txt)
w5 = "穿衣指数：%s,%s" %(drsg,drsg_txt)
w6 = "流感指数：%s,%s" %(flu,flu_txt)

print w1
print w2
print w3
print w4
print w5
print w6
