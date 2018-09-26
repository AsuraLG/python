# -*- coding: utf-8 -*-

import requests
import re
import webbrowser
import clipboard
from datetime import datetime
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import sys
import ast

# 已签到贴吧计数器
counter = 0

# 创建用户会话
session = requests.Session()

# 通用请求头
commonHeaders = {
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/15E302 UCBrowser/12.1.2.1096 Mobile'
}

# 获取当前时间戳
starttime = datetime.now()

# 从参数获取BDUSS
rawInput = sys.argv.__str__()
listInput = ast.literal_eval(rawInput)
BDUSS = listInput[1]

# 通用Cookie
commonCookies = {
	'BDUSS': BDUSS
}

# 获取包含全部关注的贴吧名称的网页
nameUrl = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?tn=bdFBW&tab=favorite'
nameResp = session.get(nameUrl, cookies = commonCookies, headers = commonHeaders)

# 从网页中生成包含全部贴吧名称的列表
only_table_class_tb = SoupStrainer('table')
nameDoc = BeautifulSoup(nameResp.text, 'html.parser', parse_only = only_table_class_tb)
nameList = [(name.text, name.get('href')[5:]) for name in nameDoc.select('a')] # name.text是可读编码的贴吧名称，name.get('href')[5:]是url编码的贴吧名称

# 对每一个贴吧，发送tbs查询请求并签到
for name  in nameList:
	# 获取每个贴吧的主页
	checkUrl = 'http://tieba.baidu.com/f?ie=utf-8&kw=' + name[0] + '&fr=search'
	checkResp = session.get(checkUrl, cookies = commonCookies, headers = commonHeaders)
	
	# 提取tbs
	tbs = re.search(r'"tbs":"(.*?)"', checkResp.text).group(1)
	
	# 实施签到
	signData = {
		'ie': 'utf-8',
		'kw': name[0],
		'tbs': str(tbs)
	}
	signUrl = 'http://tieba.baidu.com/sign/add'
	signResp = session.post(signUrl, data = signData, cookies = commonCookies, headers = commonHeaders)
	if '1101' not in signResp.text:
		counter = counter + 1

# 获取当前时间戳，计算签到用时
endtime = datetime.now()
seconds = (endtime - starttime).seconds

# 返回workflow
clipboard.set('已签到贴吧' + str(counter) + '个成功，用时' + str(seconds) + '秒')
webbrowser.open('workflow://')
