## 和风天气api
[api地址](https://dev.heweather.com/docs/api/weather)
### 请求url
```
#获取北京实况天气
https://api.heweather.net/s6/weather/now?location=beijing&key=xxx
```
参数

* location **必选参数** 需要查询的城市地址。详细见api文档。
* lang      **可选**       语言，默认为中文
* unit      **可选**        单位，米还是别的
* key       **必选**       不多说

返回参数

**ps** 以下仅列举一些，具体见api文档

*   location 城市
*   loc&utc 接口更新时间（loc为当地时间）
*   tmp&fl 温度&体感温度
*   pcpn 降水量
*   cond_text 实况天气描述

诸如此类，还有很多，用到再说。