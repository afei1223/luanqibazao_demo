import requests,json
url = 'https://free-api.heweather.net/s6/weather/now?location=宁波&key=eaf078e97dfa43f2b3471d132244477b'
res = requests.get(url)

res = json.loads(res.text)
#和我请求的weather-type相对应。
res1 = res['HeWeather6'][0]['now']

#以下三个是基本参数，所有请求都会返回。
#城市地区的基础信息
res2 = res['HeWeather6'][0]['basic']
#更新日期
res3 = res['HeWeather6'][0]['update']
#接口状态
res4 = res['HeWeather6'][0]['status']
print(res1)
print(res2)
print(res3)
print(res4)
print('城市：'+res2['location'])
print('更新日期：'+res3['loc'])
print('风向：'+res1['wind_dir'])
# print(res['cond_text'])
print('体感温度：'+res1['fl'])
print('气温：'+res1['tmp'])
# print(res['loc'])
print('降水量：'+res1['pcpn'])