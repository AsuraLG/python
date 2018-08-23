#! /usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import sys

inpath = sys.argv[1]

def main():
	sim = Image.open(inpath)
	sim = sim.convert('RGBA')
	
	(height, width) = sim.size
	for x in range(height):
		for y in range(width):
			(R, G, B, A) = sim.getpixel((x, y))
			if (R, G, B) == (0, 0, 0):
				A = 0
				sim.putpixel((x, y), (R, G, B, A))
	
	sim.save(inpath)

if __name__ == '__main__':
	main()