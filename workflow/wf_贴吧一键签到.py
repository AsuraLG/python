# -*- coding: utf-8 -*-

import requests
import re
import webbrowser
import clipboard
import datetime
import sys
import ast

# 获取当前时间戳
starttime = datetime.datetime.now()

# 从参数获取BDUSS
rawInput = sys.argv.__str__()
listInput = ast.literal_eval(rawInput)
BDUSS = listInput[1]

# 获取包含全部关注的贴吧名称的网页
nameUrl = 'https://tieba.baidu.com/?page=like';
cookies = {'BDUSS' : BDUSS}
headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/14B100 UCBrowser/10.7.5.650 Mobile'}
response = requests.get(nameUrl, cookies = cookies, headers = headers)

# 获取tbs的值
tbs = re.search(r'tbs : "(.*?)"', response.text).group(1)

# 获取全部关注的贴吧名称记录在列表names中
names = re.findall(r'(?<=<div class="forumTile_name ">).*?(?=</div>)', response.text.encode('UTF_8'))

# 遍历所有关注的贴吧名称，若没有签到则签到
for i in range(len(names)):
	match = re.search(r'<div class="forumTile_name ">' + names[i] + r'</div></div><div class="(.*?)">', response.text.encode('UTF_8'))
	if match and 'forumTile_signforumTilesign global_icon' == match.group(1):
		continue
		
	signUrl = 'http://tieba.baidu.com/mo/m/sign?tbs=' + str(tbs) + '&fid=552164&kw=' + names[i]
	requests.post(signUrl, cookies = cookies, headers = headers)

# 获取当前时间戳，计算签到用时
endtime = datetime.datetime.now()
seconds = (endtime - starttime).seconds

# 返回workflow
clipboard.set('已签到贴吧' + str(len(names)) + '个成功，用时' + str(seconds) + '秒')
webbrowser.open('workflow://')
