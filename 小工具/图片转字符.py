#! /usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw
import sys

#gray2char = list(r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^` ')
gray2char = list('#&$*o!;.')
#gray2char.reverse()
unit = (256.0)/len(gray2char)

if 3 != len(sys.argv):
	print 'Usage: python img2ascii.py [zoom] [source_path]'
	exit(0)

zoom = float(sys.argv[1]) #缩放比例，通常情况下保持为1即可
inpath = sys.argv[2]

# rgb数值和ascii字符的映射函数
def rgb2char(r, g, b, alpha = 256):
	if 0 == alpha:
		return ' '
		
	gray = int(0.299 * r + 0.587 * g + 0.114 * b) #sRGB常用公式和心理学常用公式
	#gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) #线性空间常用公式
	return gray2char[int(gray/unit)]

# 缩放函数
def func(n):
	return int(zoom * n)
	
# 获取字体对象，用于后续将ascii字符串转换成图片
def getImgFont(fontsize):
	return ImageFont.truetype(r'J:\Windows\Fonts\consolab.ttf', fontsize)
	#return ImageFont.load_default()

# 根据ascii字符集生成新图片	
def genImg(charset, fontsize = 10, bgcolor = '#FFFFFF'):
	linelist = charset.split('\n')
	font = getImgFont(fontsize)
	width, height = font.getsize(linelist[0]) #获取一行字符的宽和高
	
	image = Image.new('RGB', (width, height * len(linelist)), bgcolor) #生成新图片，背景色为纯白色
	draw = ImageDraw.Draw(image)
	
	# 将ascii字符集的每一行写入到图片中
	for y in range(len(linelist)):
		line = linelist[y]
		draw.text((0, y * height), line, font = font, fill = (0, 0, 0)) # fill为字符颜色，font为字体
		
	return image
	
def main():
	im = Image.open(inpath)
	(width, height) = map(func, im.size)
	im = im.resize((width, height), Image.ANTIALIAS)
	
	res = [[0 for i in range(width)] for i in range(height)]
	
	for x in range(width):
		for y in range(height):
			res[y][x] = rgb2char(*im.getpixel((x, y)))
	
	# 获取转换后的ASCII字符集 
	charset = ''
	for y in range(height):
		charset += ''.join(res[y])
		charset += '\n'
	charset = charset[:-1]
	
	# 首先保存文本文件
	with open('out.txt', 'w') as f:
		f.write(charset)
	
	# 再保存未resize未压缩的的字符图片
	asciiIm = genImg(charset)
	asciiIm.save('out.bmp') # 保存时使用bmp格式，可以无损保存
	
	# 最后保存缩放至和原图片比例一致的压缩后的图片
	asciiIm = asciiIm.resize((width, height), Image.ANTIALIAS)
	asciiIm.save('out_resize.jpg')

if __name__ == '__main__':
	main()