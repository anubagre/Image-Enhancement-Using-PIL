# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:48:00 2023

@author: HP
"""

'''from PIL import Image
img=Image.open(r"C:\\Users\HP\OneDrive\Pictures\canva\649-07118141en_Masterfile.jpg")
img2=img.Transpose.FLIP_LEFT_RIGHT
img2.save("corrected.jpg")'''

import opencv as cv2
img=cv2.imread(r"C:\\Users\HP\OneDrive\Pictures\canva\649-07118141en_Masterfile.jpg")
#Preparartion for CLAHE
clahe=cv2.createCLAHE()
#Convert to gray scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
enh_i=clahe.apply(gray_img)
cv2.imwrite('enhanced.jpg',enh_i)


