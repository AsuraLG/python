#coding:utf-8

import requests
import re
import webbrowser
import clipboard
import datetime
import sys
import ast

starttime = datetime.datetime.now()
rawInput = sys.argv.__str__()
listInput = ast.literal_eval(rawInput)
BDUSS = listInput[1]
#print BDUSS
infoUrl = "https://tieba.baidu.com/?page=like";
cookies = {"BDUSS" : BDUSS}
headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/14B100 UCBrowser/10.7.5.650 Mobile'}
response = requests.get(infoUrl, cookies = cookies, headers = headers)

matcher = re.findall(r'(?<=<div class="forumTile_name">).*(?=</div>)', response.text.encode('UTF_8'))
for i in range(len(matcher)):
	match = re.search(r'<div class="forumTile_name">' + matcher[i] + r'</div>\r\n\t{1,50}</div><div class="(.*?)">', response.text)
	if match and 'forumTile_signforumTilesign global_icon' == match.group(1):
		continue
		
	signUrl = "http://tieba.baidu.com/mo/m/sign?tbs=8381d2143c59d0c91491024593&fid=552164&kw=" + matcher[i]
	requests.post(signUrl, cookies = cookies, headers = headers)
	#print matcher[i]
	
endtime = datetime.datetime.now()
seconds = (endtime - starttime).seconds

clipboard.set('已签到贴吧' + str(len(matcher)) + '个成功，用时' + str(seconds) + '秒')
webbrowser.open('workflow://')
