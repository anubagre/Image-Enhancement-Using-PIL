# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:03:39 2023

@author: HP
"""

from PIL import Image
im=Image.open(r'C:/Users/HP/AppData/Local/Temp/tmpvtztuzxi.PNG')
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((1,1))
print(r,g,b)