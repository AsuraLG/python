#! /usr/bin/python
# -*- coding: utf-8 -*-

# for python3

import sys
import os
import chardet
import codecs

def writeFile(filePath, u, encoding):
	with codecs.open(filePath, 'w', encoding) as f:
		f.write(u)

def convert(src, dst, encoding = 'utf-8'):
	# 检测编码，coding可能检测不到编码，有异常
	f = open(src, 'rb')
	coding = chardet.detect(f.read())['encoding'].lower()
	f.close()
	if coding != encoding:
		with codecs.open(src, 'r', coding) as f:
			try:
				writeFile(dst, f.read(), encoding)
				try:
					print(src + ' ' + coding + ' to ' + encoding + ' converted success!')
				except Exception:
					print(src + ' ' + coding + ' to ' + encoding + ' converted fail!')
			except Exception:
				print(src + ' ' + coding + ' read error')

# 把目录中指定的文件由任何编码转换为指定编码，默认为utf-8
def work(rootdir):
	#os.walk会遍历所有子文件夹，topdown指定遍历算法，True为广度优先遍历， False为深度优先遍历
	for parent, files in os.walk(rootdir, topdown=False):
		for file in files:
			#print os.path.join(parent, file))
			if file.endswith('.sql'):
				convert(os.path.join(parent, file), os.path.join(parent, file))
		
if __name__ == '__main__':
	# 读取搜索的起始路径
	path = sys.argv[1]
	work(path)