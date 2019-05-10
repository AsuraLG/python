# -*- coding: utf-8 -*-

import requests
import re
import time
from datetime import datetime
import urllib
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# 登录后得到的BDUSS
bduss = 'FRbFR2YVZPV042Nk5tRzdXcEx2OHVYdy11QWlYU21QRUJORHYwVC1FSUk1TTFiQVFBQUFBJCQAAAAAAAAAAAEAAABd3s80bGc4MDIzbW91c2UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhXplsIV6ZbUm';

# 已签到贴吧计数器
counter = 0

# 获取当前时间戳
starttime = datetime.now()

# 创建用户会话
session = requests.Session()

# 通用请求头
commonHeaders = {
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/15E302 UCBrowser/12.1.2.1096 Mobile'
}

# 通用Cookie
commonCookies = {
	'BDUSS': bduss
}

# 获取包含全部关注的贴吧名称的网页
nameUrl = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?tn=bdFBW&tab=favorite'
sTime = datetime.now()
nameResp = session.get(nameUrl, cookies = commonCookies, headers = commonHeaders)
eTime = datetime.now()
#print u'获取包含全部关注的贴吧名称的网页用时 ' + str((eTime - sTime).microseconds) + u' 毫秒'
#print nameResp.text

# 从网页中生成包含全部贴吧名称的列表
sTime = datetime.now()
only_table_class_tb = SoupStrainer('table')
nameDoc = BeautifulSoup(nameResp.text, 'lxml', parse_only = only_table_class_tb)
#print nameDoc
nameList = [(name.text, name.get('href')[5:]) for name in nameDoc.select('a')] # name.text是可读编码的贴吧名称，name.get('href')[5:]是url编码的贴吧名称
eTime = datetime.now()
#print u'从网页中生成包含全部贴吧名称的列表用时 ' + str((eTime - sTime).microseconds) + u' 毫秒'
#print nameList

# 对每一个贴吧，发送tbs查询请求并签到
for name  in nameList:
	# 获取每个贴吧的主页，此处换成电脑浏览器的UA才可正常
	sTime = datetime.now()
	# 第一种方式
	specialHeaders = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	}
	checkUrl = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=' + name[1]
	checkResp = session.get(checkUrl, cookies = commonCookies, headers = specialHeaders)
	
	# 第二种方式
	#checkUrl = 'http://tieba.baidu.com/f?ie=utf-8&kw=' + name[0] + '&fr=search'
	#checkResp = session.get(checkUrl, cookies = commonCookies, headers = commonHeaders)
	
	#print checkUrl
	eTime = datetime.now()
	#print u'获取贴吧的主页用时 ' + str((eTime - sTime).microseconds) + u' 毫秒'
	#print checkResp.text
	#raise RuntimeError('test')
	
	# 提取tbs
	sTime = datetime.now()
	# 第一种方式
	htmlDoc = BeautifulSoup(checkResp.text, 'lxml')
	#print htmlDoc
	tbs = htmlDoc.select('input[name="tbs"]')[0].get('value')
	
	# 第二种方式
	#tbs = re.search(r'"tbs":"(.*?)"', checkResp.text).group(1)
	#print tbs
	
	eTime = datetime.now()
	#print u'提取tbs用时 ' + str((eTime - sTime).microseconds) + u' 毫秒'
	
	# 实施签到
	signData = {
		'ie': 'utf-8',
		'kw': name[0],
		'tbs': str(tbs)
	}
	signUrl = 'http://tieba.baidu.com/sign/add'
	signResp = session.post(signUrl, data = signData, cookies = commonCookies, headers = commonHeaders)
	#print signResp.text
	if '1101' not in signResp.text:
		counter = counter + 1
	
# 获取当前时间戳，计算签到用时
endtime = datetime.now()
seconds = (endtime - starttime).seconds
print u'用时 ' + str(seconds) + u' 秒，签到 ' + str(counter) + u' 个贴吧'
