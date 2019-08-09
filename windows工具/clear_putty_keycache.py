# -*- coding: utf-8 -*-

# for python3

#导入winreg模块和os模块
import winreg as winreg
import os

def main():
	try:
		# 打开保存了Putty的全部密钥指纹信息的键的父键
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\SimonTatham\PuTTY')
	
	    # 删除保存指纹信息的子键		
		winreg.DeleteKey(key, 'SshHostKeys')			
	except:
		input('Error! press any key to exit')
	else:
		input('press any key to exit')

if __name__ == "__main__":
	main()