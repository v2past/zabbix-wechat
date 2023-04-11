# zabbix-wechat
zabbix接入企业微信告警




1、将wechat.py拷贝至/usr/lib/zabbix/alertscripts/目录下，按照响应参数修改
第40行:  “toparty”:“2”, #企业部门id。

第42行： “agentid”:“100035”, #企业号中的应用id。

第61行： corpid = ‘22jsaooasbf23934’ #CorpID是企业号的标识

第62行： corpsecret = ‘410Jsk8_4lvCQYmdo92-sdfafsadfasdfxzc’ #corpsecretSecret是管理组凭证密钥

2、执行测试，python /usr/lib/zabbix/alertscripts/wechat.py aaabbbccc abc 1234

3、界面配置，打开zabbix后台
<img width="818" alt="image" src="https://user-images.githubusercontent.com/24469322/231050171-9de6ae39-17d5-4ff9-bf98-1ba469c9fa71.png">
添加3个参数，分别是{ALERT.SENDTO} 、{ALERT.SUBJECT}  、{ALERT.MESSAGE}  

4、配置动作和用户即可。

可参照：https://bbs.huaweicloud.com/blogs/374992
