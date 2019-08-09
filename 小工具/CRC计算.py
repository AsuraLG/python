#! /usr/bin/python
# -*- coding: utf-8 -*-

# for python3

import crcmod.predefined
import sys

'''
支持的算法：

8位CRC：
CRC8，CRC8Darc，CRC8ICode，CRC8Itu，CRC8Maxim，CRC8Rohc，CRC8Wcdma

16位CRC：
CRC16，CRC16Buypass，CRC16Dds110，CRC16Dect，CRC16Dnp，CRC16En13757，CRC16Genibus，CRC16Maxim，CRC16Mcrf4xx，CRCX25
CRC16Riello，CRC16T10Dif，CRC16Teledisk，CRC16Usb，CRCXmodem，CRCModbus，CRCKermit，CRCCcittFalse，CRCAugCcitt

24位CRC：
CRC24，CRC24FlexrayA，CRC24FlexrayB

32位CRC：
CRC32，CRC32Bzip2，CRC32C，CRC32D，CRC32Mpeg，CRCPosix，CRC32Q，CRCJamCrc，CRCXfer

64位CRC：
CRC64，CRC64We，CRC64Jones
'''


def main():
	print('''8bitCRC：
CRC8，CRC8Darc，CRC8ICode，CRC8Itu，CRC8Maxim，CRC8Rohc，CRC8Wcdma

16bitCRC：
CRC16，CRC16Buypass，CRC16Dds110，CRC16Dect，CRC16Dnp，CRC16En13757，CRC16Genibus，CRC16Maxim，CRC16Mcrf4xx，CRCX25，CRC16Riello，CRC16T10Dif，CRC16Teledisk，CRC16Usb，CRCXmodem，CRCModbus，CRCKermit，CRCCcittFalse，CRCAugCcitt

24bitCRC：
CRC24，CRC24FlexrayA，CRC24FlexrayB

32bitCRC：
CRC32，CRC32Bzip2，CRC32C，CRC32D，CRC32Mpeg，CRCPosix，CRC32Q，CRCJamCrc，CRCXfer

64bitCRC：
CRC64，CRC64We，CRC64Jones
''')
	type = input('算法类型: ')
	str = input('字符串: ')
	crcGen = crcmod.predefined.mkPredefinedCrcFun(type)
	print('结果为：0x'+hex(crcGen(str.encode())).upper()[2:])
	input('请按下任意键退出');
	
if __name__ == '__main__':
	main()
