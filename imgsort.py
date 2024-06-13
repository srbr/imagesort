import os
import sys
from PIL import Image, ImageFilter

if __name__ == '__main__':
	args = sys.argv
	argl = len(args)
	if 2 <= argl:
		for i in range(1, argl):
			with Image.open(args[i]) as src:
				w = src.size[0]
				h = src.size[1]
				src_hsv = src.convert('HSV')
				dst_hsv = Image.new('HSV', (w, h))
				color_list = [src_hsv.getpixel((x, y)) for x in range(w) for y in range(h)]
				color_list.sort(key=lambda l: (l[1], l[2], l[0]))
				n = 0
				for y in range(h):
					for x in range(w):
						dst_hsv.putpixel((x, y), color_list[n])
						n += 1
				dst_hsv.convert('RGB').save(os.path.splitext(args[i])[0] + '_sorted.png')