# -*- coding: utf-8 -*-

# for python3

#导入winreg模块和os模块
import winreg, os

def main():
	try:
		pass
		#获取键
		key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'Local Settings\Software\Microsoft\Windows\CurrentVersion')
	
		#删除键
		winreg.DeleteKey(key, 'TrayNotify')
	except:
		input('no such key! press any key to exit')
	else:
		while(0 == os.system('taskkill /F /IM explorer.exe')):
			pass
		os.system('start explorer.exe')
		input('press any key to exit')

if __name__ == "__main__":
	main()