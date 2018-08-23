# -*- coding: utf-8 -*-

#导入winreg模块和os模块
import _winreg, os

def main():
	try:
		pass
		#获取键
		key = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, r'Local Settings\Software\Microsoft\Windows\CurrentVersion')
	
		#删除键
		_winreg.DeleteKey(key, 'TrayNotify')
	except:
		raw_input('no such key! press any key to exit')
	else:
		while(0 == os.system('taskkill /F /IM explorer.exe')):
			pass
		os.system('start explorer.exe')
		raw_input('press any key to exit')

if __name__ == "__main__":
	main()