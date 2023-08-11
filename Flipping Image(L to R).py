# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:38:58 2023
@author: HP
"""
#Flippin Image(L to R)
from PIL import Image
img=Image.open('corrected.jpg')
t_img=img.transpose(Image.FLIP_LEFT_RIGHT)
t_img.save('new.jpg')
